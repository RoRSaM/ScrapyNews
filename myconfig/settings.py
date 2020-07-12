class BaseConfig():
	TESTING = False
	DEBUG = False


class DEVConfig(BaseConfig):
	PORT=7000
	FLASK_ENV = 'development'
	MONGO_URL = "mongodb+srv://scraper:scraper@scrapynews.4kun9.mongodb.net/news_dev?retryWrites=true&w=majority"
	MONGO_DB = "news_dev"
	MONGO_COLLECTION = "TheGuardian"
	DEBUG = True

class PRDConfig(BaseConfig):
	PORT=8888
	FLASK_ENV = 'production'
	MONGO_URL="mongodb+srv://scraper:scraper@scrapynews.4kun9.mongodb.net/news_prod?retryWrites=true&w=majority"
	MONGO_DB = "news_prod"
	MONGO_COLLECTION = "TheGuardian"

class QLFConfig(BaseConfig):
	PORT=8000
	FLASK_ENV = 'development'
	MONGO_URL="mongodb+srv://scraper:scraper@scrapynews.4kun9.mongodb.net/news_qualif?retryWrites=true&w=majority"
	MONGO_DB = "news_qualif"
	MONGO_COLLECTION = "TheGuardian"
	TESTING = True
	DEBUG = True
