# Location: C:\optical_system\backend\start_waitress.py
import os, logging
from waitress import serve

logging.basicConfig(filename='server.log', level=logging.INFO)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'optical.settings')

from optical.wsgi import application

serve(
    application,
    host='0.0.0.0',        # Accept from all LAN clients
    port=8000,
    threads=8,             # Good for < 10 users
    connection_limit=100,
    cleanup_interval=30,
    channel_timeout=120,
)
