import json
import os
from core.config_models import Config


def load_config(env: str) -> Config:
    config_path = f"config/config_{env}.json"
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file not found: {config_path}")

    with open(config_path) as config_file:
        config_data = json.load(config_file)

    return Config(**config_data)
