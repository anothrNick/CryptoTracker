import os
from dotenv import Dotenv
dotenv = Dotenv(os.path.join(os.path.dirname(__file__), "default.env"))
os.environ.update(dotenv)

#timers in seconds
MARKET_REFRESH_RATE=1
RETRY_RATE=5
API_TIMEOUT=2

LOGLEVEL = os.environ.get("TRACKER_LOG_LEVEL")
INITIAL_SLEEP = int(os.environ.get("INITIAL_SLEEP"))

ELASTICSEARCH_CONNECT_STRING = os.environ.get("ELASTICSEARCH_CONNECT_STRING")
