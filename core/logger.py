import logging
import os
from datetime import datetime
from core.settings import load_config

def setup_logger():
    cfg = load_config()
    log_dir = cfg["paths"]["logs"]
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, f"secureone_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")

    logging.basicConfig(
        level=getattr(logging, cfg["log_level"].upper(), "INFO"),
        format="%(asctime)s | %(levelname)s | %(message)s",
        handlers=[
            logging.FileHandler(log_file, encoding="utf-8"),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger("SecureOne")

logger = setup_logger()
