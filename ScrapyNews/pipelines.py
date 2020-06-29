# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymongo

class ScrapynewsPipeline:
    def process_item(self, item, spider):
        return item

class JsonWriterPipeline:

    def open_spider(self, spider):
        self.file = open('items.jl', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item

class MongoDBWriterPipeline:

	def __init__(self):
		self.conn = pymongo.MongoClient("mongodb+srv://scraper:scraper@scrapynews.4kun9.mongodb.net/news?retryWrites=true&w=majority")
		db = self.conn['news']
		self.collection = db['TheGuardian']
	
	def process_item(self, item, spider):
		self.collection.insert(dict(item))
		return item
	