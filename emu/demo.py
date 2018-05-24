###########################################################
# Demo WPS service for testing and debugging.
#
# See the werkzeug documentation on how to use the debugger:
# http://werkzeug.pocoo.org/docs/0.12/debug/
###########################################################

import os
from jinja2 import Environment, PackageLoader, select_autoescape
from pywps import configuration

from . import wsgi
from six.moves.urllib.parse import urlparse

import logging
logging.basicConfig(format='%(message)s', level=logging.INFO)
LOGGER = logging.getLogger('DEMO')

template_env = Environment(
    loader=PackageLoader('emu', 'templates'),
    autoescape=select_autoescape(['yml', 'xml'])
)


def write_user_config(**kwargs):
    config_templ = template_env.get_template('pywps.cfg')
    rendered_config = config_templ.render(**kwargs)
    config_file = os.path.abspath(os.path.join(os.path.curdir, "custom.cfg"))
    with open(config_file, 'w') as fp:
        fp.write(rendered_config)
    return config_file


def get_host():
    url = configuration.get_config_value('server', 'url')
    url = url or 'http://localhost:5000/wps'

    LOGGER.warn("starting WPS service on %s", url)

    parsed_url = urlparse(url)
    if ':' in parsed_url.netloc:
        host, port = parsed_url.netloc.split(':')
        port = int(port)
    else:
        host = parsed_url.netloc
        port = 80
    return host, port


def _run(application, bind_host=None, daemon=False):
    from werkzeug.serving import run_simple
    # call this *after* app is initialized ... needs pywps config.
    host, port = get_host()
    bind_host = bind_host or host
    # need to serve the wps outputs
    static_files = {
        '/outputs': configuration.get_config_value('server', 'outputpath')
    }
    run_simple(
        hostname=bind_host,
        port=port,
        application=application,
        use_debugger=False,
        use_reloader=False,
        threaded=True,
        # processes=2,
        use_evalex=not daemon,
        static_files=static_files)


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="""Script for starting a demo WPS.
                       This service is by default available at http://localhost:5000/wps""",
        epilog="""Do not use this service in a production environment.
         It's intended to be running in a test environment only!
         For more documentation, visit http://pywps.org/doc
        """
    )
    parser.add_argument('-c', '--config',
                        help="path to pywps configuration file")
    parser.add_argument('-a', '--all-addresses',
                        action='store_true', help="run service using IPv4 0.0.0.0 (all network interfaces), "
                        "otherwise bind to 127.0.0.1 (localhost).")
    parser.add_argument('-d', '--daemon',
                        action='store_true', help="run in daemon mode")
    parser.add_argument('-H', '--hostname', default='localhost',
                        help="hostname in PyWPS configuration")
    parser.add_argument('-p', '--port', default='5000',
                        help="port in PyWPS configuration")
    parser.add_argument('--maxsingleinputsize', default='200mb',
                        help="maxsingleinputsize in PyWPS configuration")
    parser.add_argument('--maxprocesses', default='10',
                        help="maxprocesses in PyWPS configuration")
    parser.add_argument('--parallelprocesses', default='2',
                        help="parallelprocesses in PyWPS configuration")
    parser.add_argument('-l', '--log-level', default='INFO',
                        help="log level in PyWPS configuration")
    parser.add_argument('-o', '--log-file', default='pywps.log',
                        help="log file in PyWPS configuration")
    parser.add_argument('-D', '--database', default='sqlite:///pywps-logs.sqlite',
                        help="database in PyWPS configuration")
    args = parser.parse_args()
    cfgfiles = []
    cfgfiles.append(write_user_config(
        wps_hostname=args.hostname,
        wps_port=args.port,
        wps_maxprocesses=args.maxprocesses,
        wps_parallelprocesses=args.parallelprocesses,
        wps_log_level=args.log_level,
        wps_log_file=args.log_file,
        wsp_database=args.database,
    ))
    if args.config:
        cfgfiles.append(args.config)
        LOGGER.warn('using pywps configuration: %s', args.config)
    if args.all_addresses:
        bind_host = '0.0.0.0'
    else:
        bind_host = '127.0.0.1'
    app = wsgi.create_app(cfgfiles)
    # let's start the service ...
    # See:
    # * https://github.com/geopython/pywps-flask/blob/master/demo.py
    # * http://werkzeug.pocoo.org/docs/0.14/serving/
    if args.daemon:
        # daemon (fork) mode
        pid = None
        try:
            pid = os.fork()
            if pid:
                LOGGER.warn('forked process id: %s', pid)
        except OSError as e:
            raise Exception("%s [%d]" % (e.strerror, e.errno))

        if pid == 0:
            os.setsid()
            _run(app, bind_host=bind_host, daemon=True)
        else:
            os._exit(0)
    else:
        # no daemon
        _run(app, bind_host=bind_host)


if __name__ == '__main__':
    main()
