# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WhetherscrapeItem(scrapy.Item):
    date_time = scrapy.Field()
    kion = scrapy.Field()
    shitsudo = scrapy.Field()
