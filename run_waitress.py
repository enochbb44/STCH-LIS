import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)

from dotenv import load_dotenv
load_dotenv(os.path.join(BASE_DIR, '.env'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pcs_project.settings')

from waitress import serve
from pcs_project.wsgi import application

# Route Waitress's access/error output to the log files in <project>\logs so
# issues can be diagnosed even though the server runs as a hidden background
# process with no visible console. Waitress 3.x logs via the ``waitress``
# logger; give it file handlers here (Django's own logs are handled by
# settings.LOGGING).
import logging
from logging.handlers import RotatingFileHandler

LOG_DIR = os.path.join(BASE_DIR, 'logs')
os.makedirs(LOG_DIR, exist_ok=True)

_waitress_logger = logging.getLogger('waitress')
_waitress_logger.setLevel(logging.INFO)
if not _waitress_logger.handlers:
    _fmt = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    _access = RotatingFileHandler(
        os.path.join(LOG_DIR, 'access.log'),
        maxBytes=5 * 1024 * 1024, backupCount=5,
    )
    _access.setFormatter(_fmt)
    _waitress_logger.addHandler(_access)
    # Errors also go to errors.log for easy troubleshooting.
    _err = RotatingFileHandler(
        os.path.join(LOG_DIR, 'errors.log'),
        maxBytes=5 * 1024 * 1024, backupCount=5,
    )
    _err.setLevel(logging.ERROR)
    _err.setFormatter(_fmt)
    _waitress_logger.addHandler(_err)

HOST = os.environ.get('SERVER_HOST', '0.0.0.0')
PORT = int(os.environ.get('SERVER_PORT', '8000'))

# threads=32 so large/many-file archive uploads don't stall when all
# worker threads are busy; channel_timeout raised so slow uploads don't get
# dropped while the client is still sending the body.
#
# trusted_proxy / clear_untrusted_proxy_headers: when the site runs behind a
# TLS-terminating reverse proxy on this machine, the proxy forwards requests
# with X-Forwarded-Proto: https. Only the loopback proxy is trusted with that
# header; direct LAN clients are not, so they cannot spoof HTTPS.
serve(
    application,
    host=HOST,
    port=PORT,
    threads=32,
    channel_timeout=600,
    ident='pcs-lis',
    trusted_proxy='127.0.0.1',
    clear_untrusted_proxy_headers=True,
)
