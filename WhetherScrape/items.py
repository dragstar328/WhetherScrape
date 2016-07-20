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

    wheather = scrapy.Field() # tenki all
    prob_precip = scrapy.Field() # kousui kakuritsu all
    precipitation = scrapy.Field() # kousuiryou all
    wind_blow = scrapy.Field() # kazamuki all
    wind_blow2 = scrapy.Field() # kazamuki tommorow and day after tommorow
    wind_speed = scrapy.Field() # fuusoku all

