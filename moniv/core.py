import traceback
from datetime import datetime
from .transport import send_error

class Moniv:
    def __init__(self, dsn=None):
        """
        Initialize Moniv client
        dsn: optional, where to send errors (URL, API key, etc)
        """
        self.dsn = dsn

    def capture_exception(self, exc: Exception, context: dict = None):
        """
        Capture an exception and send it
        """
        error_info = {
            "type": type(exc).__name__,
            "message": str(exc),
            "traceback": traceback.format_exc(),
            "timestamp": datetime.utcnow().isoformat(),
            "context": context or {}
        }
        send_error(error_info, self.dsn)