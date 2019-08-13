# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Baojun002Item(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    price = scrapy.Field()
    destination = scrapy.Field()
    subhead = scrapy.Field()
    intro = scrapy.Field()
    include = scrapy.Field()
    day = scrapy.Field()
    night = scrapy.Field()
    journeys = scrapy.Field()
    scenic_images = scrapy.Field()
    departure = scrapy.Field()
    tickets = scrapy.Field()
