# Scrapy News

## Description
The main purpose of the project is to **retrieve** data from configured **news** websites (like BBC, The Guardian …) and store it on **MongoDB**.

It will allow also final users to read, list and search stored news via **Restful** calls.

So the project will contains two main modules: 

### Scraper
This module is responsible for:

*  Scrapping news from websites.
*  Cleaning data.
*  Storing data on MongoDB.

		
### Restful API
This module will allow users to:

*	**Read** & **list** available documents on MongoDB.
*	**Search** articles by title, author or keyword.
		
## Branches
The project has two main branches: 
	
**Master branch:** Represent a stable working version of the project.
	
**Dev branch:** Dedicated for continuous dev/modification (fixing bugs, adding features, etc.)
	
## Dependencies

*	**Scrapy:** Web crawling framework, used to extract data from web page with the help of selectors.
		
*	**PyMongo:** The official driver for connecting a python project with mongodb.
		
*	**Flask:** Web application framework.
		
*	**Flask-PyMongo:** Integrates pymongo with Flask.
		
*	**DNSPython:** Manages the translation of domain names to IP adress.
		
*	**PyOpenSSL:** Wrapper around the OpenSSL library.

## Installation
### 1.	Install Python
Please install in your operating system **python version 3 or heigher**.

### 2.	Download source code to your local environment
`git clone https://github.com/RoRSaM/ScrapyNews.git`

### 3.	Go inside the project folder
`cd scrapynews`

### 4.	Install dependencies
`pip install -r requirements.txt`
		
## Run Project
The project is supposed to run in one of the following environments: 

*	__DEV:__ Developement environment.
*	__QLF:__ Qualification/Test environment.
*	__PRD:__ Production environment.

Please perform your validation tests in qualification environment by exporting a new global environment variable : 
`export APP_ENV=QLF`

### 1.	Run Scrapping module
`scrapy crawl TheGuardian`

The logique consists of collecting news published in day **(today - 1 = yesterday)**.

You can create an entry in the crontab to run the above command every day at a specific time.
	
### 2.	Run Web Server
`./runServer`

The web server is configured to listen on port 7000.

available services are:

*	__/getAll:__		Get all articles
*	__/getByTitle/*<title\>*:__ Get article with the given title
*	__/getByAuthor/*<author\>*:__ Get all articles writed by the given author
*	__/getByKeyword/*<keyword\>*:__ Get all articles that contains the given keyword

## So what's next ?
Future features will concerne mainly adding new websites sources and why not deducing and implementing a common pattern for data retrieving from differents news websites.

So the next step focus on describing selectors with a config file.
