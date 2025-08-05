import datetime
from config.settings import settings

def get_tstamp():
	return datetime.date.today()

def set_tstamp(stamp: str):
	return datetime.datetime.strptime(stamp, '%Y-%m-%d').date()

def get_scrap_date():
	start_stamp = datetime.datetime.strptime(settings.get('SCRAP_DATE_START'), "%Y-%m-%d")
	end_stamp = datetime.datetime.strptime(settings.get('SCRAP_DATE_END'), "%Y-%m-%d")
	return {'start': {'year': start_stamp.year, 'month': start_stamp.month, 'day': start_stamp.day}, 'end': {'year': end_stamp.year, 'month': end_stamp.month, 'day': end_stamp.day}}
