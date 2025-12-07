import json
from pathlib import Path

LOG_FILE = Path("moniv_errors.log")

def send_error(error_info: dict, dsn=None):
    """
    Save error to a file or send it somewhere (if DSN provided)
    """
    if dsn:
        # TODO: implement HTTP sending to server
        pass

    # Save locally
    with LOG_FILE.open("a") as f:
        f.write(json.dumps(error_info) + "\n")