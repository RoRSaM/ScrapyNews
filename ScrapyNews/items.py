# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class TheGuardianItem(scrapy.Item):

	domain = scrapy.Field()
	subDomain = scrapy.Field()
	createdBy = scrapy.Field()
	updatedBy = scrapy.Field()
	title = scrapy.Field()
	author = scrapy.Field()
	article = scrapy.Field()
	link = scrapy.Field()