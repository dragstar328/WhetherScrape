# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WhetherscrapeItem(scrapy.Item):
    body = scrapy.Field() # today and tommorow
    body2 = scrapy.Field() # day after tommorow
    kion = scrapy.Field() # all
    shitsudo = scrapy.Field() # today
    shitsudo2 = scrapy.Field() # tommorow and day after tommorow

