import os
from .dev_config import DevConfig
from .base_config import BaseConfig

class Settings:
	def __init__(self):
		environment = os.getenv('DEBUG', None) == 'True'
	
		# Ortama göre doğru ayarları yükle
		# environment = os.getenv("FLASK_ENV", "development").lower()
		if (environment):
			self.config = DevConfig
		else:
			self.config = BaseConfig

	def get(self, setting_name):
		return getattr(self.config, setting_name, None)

settings = Settings()
