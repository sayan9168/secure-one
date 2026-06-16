import json
import os

CONFIG_PATH = "config.json"

def load_config():
    if not os.path.exists(CONFIG_PATH):
        default = {
            "app_name": "Secure-One",
            "version": "1.0.0",
            "default_timeout": 2,
            "max_threads": 50,
            "log_level": "INFO",
            "report_format": "html",
            "save_reports": True,
            "interfaces": {"linux": "eth0", "termux": "wlan0", "windows": "Wi-Fi"},
            "paths": {"logs": "./logs/", "reports": "./reports/", "wordlists": "./wordlists/"},
            "shodan_api_key": "",
            "safe_mode": True
        }
        with open(CONFIG_PATH, "w") as f:
            json.dump(default, f, indent=4)
    with open(CONFIG_PATH, "r") as f:
        return json.load(f)

def save_config(new_config):
    with open(CONFIG_PATH, "w") as f:
        json.dump(new_config, f, indent=4)
      
