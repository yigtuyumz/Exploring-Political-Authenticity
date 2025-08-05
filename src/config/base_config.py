import os
from dotenv import load_dotenv

load_dotenv()

class BaseConfig:
	SCRAP_ACCOUNTS = os.getenv('SCRAP_ACCOUNTS', None).split(',')
	SCRAP_DATE_START = os.getenv('SCRAP_DATE_START', None)
	SCRAP_DATE_END = os.getenv('SCRAP_DATE_END', None)