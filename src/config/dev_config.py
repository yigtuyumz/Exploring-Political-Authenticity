# src/config/dev_config.py
import os
from .base_config import BaseConfig

class DevConfig(BaseConfig):
	API_KEY = os.getenv('API_KEY', None)
