import scrapy
import configparser
import os
import logging
from ..items import TheGuardianItem

from datetime import date, timedelta,datetime

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
		for link in response.css("ul.subnav__list").css("li.subnav__item").css("a.subnav-link"):
			links.append(link.attrib['href'])
		
		uLinks=set(links)
		yield scrapy.Request(url=links[0], callback=self.getArticles)

		#for link in uLinks:
		#	yield scrapy.Request(url=link, callback=self.getArticles)
			
			
	def getArticles(self, response):
		links=response.css("div.fc-item__container").css("div.fc-item__content").css("div.fc-item__header").css("h3.fc-item__title").css("a.fc-item__link")
		for link in response.css("div.fc-item__container").css("div.fc-item__content").css("div.fc-item__header").css("h3.fc-item__title").css("a.fc-item__link"):
			yield scrapy.Request(url=link.attrib['href'], callback=self.parseArticle)

			
		
	def parseArticle(self, response):
		article = TheGuardianItem()
		article['link']=response.url
		article['title']=response.css("h1.content__headline::text").extract_first()
		article['author']=response.css("div.meta__contact-wrap").css("p.byline").css("a").css("span::text").extract_first()
		#article['createdBy']=response.css("div.meta__contact-wrap").css("p.content__dateline").css("time")[0].attrib['datetime']
		#article['updatedBy']=response.css("div.meta__contact-wrap").css("p.content__dateline").css("time")[1].attrib['datetime']
		articleBody=''
		article['article']=response.css("div.content__article-body").css("p::text").extract()
		#for p in response.css("div.content__article-body").css("p"):
		#	articleBody=articleBody + '\n' + p.css("text").extract_first()
		#article['article']=articleBody
		yield article
	
	def parseURL(self, url):
		yasterday=date.today() - timedelta(days=1)
		day=yasterday.strftime("%d")
		mon=yasterday.strftime("%B")[:3]
		year=yasterday.strftime("%Y")
		return url+'/'+year+'/'+mon+'/'+day+'/all'
