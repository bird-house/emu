# Application
APP_ROOT := $(CURDIR)
APP_NAME := $(shell basename $(APP_ROOT))

# Anaconda
CONDA := $(shell command -v conda 2> /dev/null)
ANACONDA_HOME := $(shell conda info --base 2> /dev/null)
CONDA_ENV ?= $(APP_NAME)

TEMP_FILES := *.egg-info *.log *.sqlite

# end of configuration

.DEFAULT_GOAL := all

.PHONY: all
all: help
ifndef CONDA
	$(error "Conda is not available. Please install miniconda: https://conda.io/miniconda.html")
endif

.PHONY: help
help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  help        to print this help message. (Default)"
	@echo "  install     to install $(APP_NAME) by running 'python setup.py develop'."
	@echo "  start       to start $(APP_NAME) service as daemon (background process)."
	@echo "  stop        to stop $(APP_NAME) service."
	@echo "  status      to show status of $(APP_NAME) service."
	@echo "  clean       to remove *all* files that are not controlled by 'git'. WARNING: use it *only* if you know what you do!"
	@echo "\nTesting targets:"
	@echo "  test        to run tests (but skip long running tests)."
	@echo "  testall     to run all tests (including long running tests)."
	@echo "  pep8        to run pep8 code style checks."
	@echo "\nSphinx targets:"
	@echo "  docs        to generate HTML documentation with Sphinx."

## Anaconda targets

.PHONY: conda_env
conda_env:
	@echo "Updating conda environment $(CONDA_ENV) ..."
	"$(CONDA)" env update -n $(CONDA_ENV) -f environment.yml

## Build targets

.PHONY: bootstrap
bootstrap: conda_env bootstrap_dev
	@echo "Bootstrap ..."

.PHONY: bootstrap_dev
bootstrap_dev:
	@echo "Installing development requirements for tests and docs ..."
	@-bash -c "$(CONDA) install -y -n $(CONDA_ENV) pytest flake8 sphinx bumpversion"
	@-bash -c "source $(ANACONDA_HOME)/bin/activate $(CONDA_ENV) && pip install -r requirements_dev.txt"

.PHONY: install
install: bootstrap
	@echo "Installing application ..."
	@-bash -c "source $(ANACONDA_HOME)/bin/activate $(CONDA_ENV) && python setup.py develop"
	@echo "\nStart service with \`make start'"

.PHONY: start
start:
	@echo "Starting application ..."
	@-bash -c "source $(ANACONDA_HOME)/bin/activate $(CONDA_ENV) && $(APP_NAME) start -d"

.PHONY: stop
stop:
	@echo "Stopping application ..."
	@-bash -c "source $(ANACONDA_HOME)/bin/activate $(CONDA_ENV) && $(APP_NAME) stop"

.PHONY: status
status:
	@echo "Show status ..."
	@-bash -c "source $(ANACONDA_HOME)/bin/activate $(CONDA_ENV) && $(APP_NAME) status"

.PHONY: clean
clean: srcclean envclean
	@echo "Cleaning generated files ..."
	@-for i in $(TEMP_FILES); do \
  	test -e $$i && rm -v -rf $$i; \
  done

.PHONY: envclean
envclean:
	@echo "Removing conda env $(CONDA_ENV)"
	@-"$(CONDA)" remove -n $(CONDA_ENV) --yes --all

.PHONY: srcclean
srcclean:
	@echo "Removing *.pyc files ..."
	@-find $(APP_ROOT) -type f -name "*.pyc" -print | xargs rm

.PHONY: distclean
distclean: clean
	@echo "Cleaning ..."
	@git diff --quiet HEAD || echo "There are uncommited changes! Not doing 'git clean' ..."
	@-git clean -dfx -e *.bak -e custom.cfg

## Test targets

.PHONY: test
test:
	@echo "Running tests (skip slow and online tests) ..."
	@-bash -c "source $(ANACONDA_HOME)/bin/activate $(CONDA_ENV);pytest -v -m 'not slow and not online'"

.PHONY: testall
testall:
	@echo "Running all tests (including slow and online tests) ..."
	@-bash -c "source $(ANACONDA_HOME)/bin/activate $(CONDA_ENV) && pytest -v"

.PHONY: pep8
pep8:
	@echo "Running pep8 code style checks ..."
	@-bash -c "source $(ANACONDA_HOME)/bin/activate $(CONDA_ENV) && flake8"

##  Sphinx targets

.PHONY: docs
docs:
	@echo "Generating docs with Sphinx ..."
	@-bash -c "source $(ANACONDA_HOME)/bin/activate $(CONDA_ENV);$(MAKE) -C $@ clean html"
	@echo "open your browser: firefox docs/build/html/index.html"
