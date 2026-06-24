import json
import logging
import sys
from datetime import datetime

logger = logging.getLogger()
logger.setLevel(logging.INFO)

if logger.handlers:
    logger.handlers.clear()

handler = logging.StreamHandler(sys.stdout)
logger.addHandler(handler)


def log(level, service, message, **kwargs):

    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "level": level,
        "service": service,
        "message": message
    }

    log_entry.update(kwargs)

    logger.info(json.dumps(log_entry))