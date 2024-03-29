# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient


class QunawangPipeline(object):
    def open_spider(self, spider):
        client = MongoClient(host="127.0.0.1", port=27017)
        self.db = client.travel

    def process_item(self, item, spider):
        item = dict(item)
        self.db.scheme.insert(item)
        return item

    def close_spider(self, spider):
        pass
