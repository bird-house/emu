# Application
APP_ROOT := $(CURDIR)
APP_NAME := $(shell basename $(APP_ROOT))

# Anaconda
ANACONDA_HOME := $(HOME)/anaconda
CONDA_ENV := $(APP_NAME)

# Choose Anaconda installer depending on your OS
ANACONDA_URL = https://repo.continuum.io/miniconda
ifeq "$(OS_NAME)" "Linux"
FN := Miniconda3-latest-Linux-x86_64.sh
else ifeq "$(OS_NAME)" "Darwin"
FN := Miniconda3-latest-MacOSX-x86_64.sh
else
FN := unknown
endif

# end of configuration

.DEFAULT_GOAL := all

.PHONY: all
all: help

.PHONY: help
help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  help        to print this help message. (Default)"
	@echo "  install     to install $(APP_NAME) in Conda environment $(CONDA_ENV) by running 'python setup.py develop'."
	@echo "  clean       to remove *all* files that are not controlled by 'git'. WARNING: use it *only* if you know what you do!"

## Anaconda targets

.PHONY: anaconda
anaconda:
	@echo "Installing Anaconda ..."
	@test -d $(ANACONDA_HOME) || curl $(ANACONDA_URL)/$(FN) --silent --insecure --output "$(DOWNLOAD_CACHE)/$(FN)"
	@test -d $(ANACONDA_HOME) || bash "$(DOWNLOAD_CACHE)/$(FN)" -b -p $(ANACONDA_HOME)
	@echo "Add '$(ANACONDA_HOME)/bin' to your PATH variable in '.bashrc'."

.PHONY: conda_env
conda_env: anaconda
	@echo "Update conda environment $(CONDA_ENV) ..."
	"$(ANACONDA_HOME)/bin/conda" env update -n $(CONDA_ENV) -f environment.yml

## Build targets

.PHONY: bootstrap
bootstrap: conda_env
	@echo "Bootstrap ..."

.PHONY: install
install: bootstrap
	@echo "Installing application ..."
	@-bash -c "source $(ANACONDA_HOME)/bin/activate $(CONDA_ENV) && python setup.py develop"
	@echo "\nStart service with \`make start'"

.PHONY: clean
clean:
	@echo "Cleaning ..."
	@git diff --quiet HEAD || echo "There are uncommited changes! Not doing 'git clean' ..."
	@-git clean -dfx -e *.bak -e custom.cfg
