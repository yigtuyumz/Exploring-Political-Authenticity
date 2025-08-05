from config import settings
from tests import get_date_timestamp
from config.settings import settings
from tests.httpserver import server

def main():
	print("Hello, main!")
	print(get_date_timestamp.get_tstamp())
	print(get_date_timestamp.set_tstamp('1999-01-01'))
	print(settings.get('SCRAP_ACCOUNTS'))
	print(get_date_timestamp.get_scrap_date().get('start').get('year'))
	server.server.start()


if __name__ == '__main__':
	main()
