import logging
import sys
import json
from datetime import datetime

class JsonFormatter(logging.Formatter):
    """
    Custom JSON formatter for structured logging
    """
    def format(self, record):
        log_record = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "level": record.levelname,
            "name": record.name,
            "message": record.getMessage(),
        }

        # Include exception info if present
        if record.exc_info:
            log_record["exc_info"] = self.formatException(record.exc_info)

        return json.dumps(log_record)


# Create logger
logger = logging.getLogger("inventory_app")
logger.setLevel(logging.DEBUG)  # Can be DEBUG, INFO, WARNING, ERROR, CRITICAL

# Console handler
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(JsonFormatter())

logger.addHandler(console_handler)