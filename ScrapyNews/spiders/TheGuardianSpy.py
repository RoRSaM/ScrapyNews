import scrapy
import configparser
import os
import logging
from ..items import TheGuardianItem
from datetime import date, timedelta, datetime

class TheGuardianSpy(scrapy.Spider):
	name = "TheGuardian"
	start_urls = [
		"https://www.theguardian.com/international"
	]
	def __init__(self):
		self.path = os.getcwd()
		self.env = os.getenv('ENV', default='DEV').lower()
		self.config = configparser.RawConfigParser()
		self.config.read(self.path+'/config/app.'+self.env+'.properties')
	
	def sendRequests(self):
		yield scrapy.Request(url=start_urls, callback=self.parse)
								
	def parse(self, response):
		links=[]
		for link in response.css("ul.pillars").css("li.pillars__item").css("a.pillar-link"):
			links.append(link.attrib['href'])
			
		uLinks=set(links)
		yield scrapy.Request(url=links[0], callback=self.subParse)
		#for link in uLinks:
		#	yield scrapy.Request(url=link, callback=self.subParse)
			

	def subParse(self, response):
		links=[]
		day=date.today() - timedelta(days=1)
		urlDay=day.strftime("%Y/%b/%d")+"/all"
		for link in response.css("ul.subnav__list").css("li.subnav__item").css("a.subnav-link"):
			links.append(link.attrib['href']+"/"+urlDay)
		
		uLinks=set(links)
		for link in uLinks:
			yield scrapy.Request(url=link, callback=self.getArticles)
			
			
	def getArticles(self, response):
		links=response.css("div.fc-item__container").css("div.fc-item__content").css("div.fc-item__header").css("h3.fc-item__title").css("a.fc-item__link")
		for link in links:
			yield scrapy.Request(url=link.attrib['href'], callback=self.parseArticle)
			
		
	def parseArticle(self, response):
		article = TheGuardianItem()
		article['link']=response.url
		article['category']=response.url.split('/')[3]
		article['title']=response.css("h1.content__headline::text").extract_first()
		
		author=response.css("div.meta__contact-wrap").css("p.byline").css("a").css("span::text").extract_first()
		if author is None:
			author=response.css("div.meta__contact-wrap").css("p.byline").extract_first()	
		article['author']=author
		dataTimeStamp=response.css("div.meta__contact-wrap").css("p.content__dateline").css("time.content__dateline-wpd").attrib['data-timestamp']
		article['date']= datetime.fromtimestamp(int(dataTimeStamp)/1000).strftime("%Y-%m-%d %H:%M:%S")
		article['article']=response.css("div.content__article-body").css("p::text").extract()
		yield article
	
	def parseURL(self, url):
		yasterday=date.today() - timedelta(days=1)
		day=yasterday.strftime("%d")
		mon=yasterday.strftime("%B")[:3]
		year=yasterday.strftime("%Y")
		return url+'/'+year+'/'+mon+'/'+day+'/all'
