# -*- coding: utf-8 -*-

"""Top-level package for Emu."""

from .__version__ import __author__, __email__, __version__

from pywps.application import make_app

application = make_app()
