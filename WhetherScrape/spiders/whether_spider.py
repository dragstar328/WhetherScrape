# -*- coding: utf-8 -*-
import scrapy
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http.request import Request
from WhetherScrape.items import WhetherscrapeItem
from scrapy.selector import Selector

class TenkiJpSpider(scrapy.Spider):
	name = "TenkiJp"
	allowed_domains = ["tenki.jp"]
	start_urls = [
		"http://www.tenki.jp/forecast/5/26/5110/23100-1hour.html"
	]
	
	def parse(self, response):
		item = WhetherscrapeItem()
		sel = Selector(response)
		
		item['body'] = sel.xpath('//table[@class="leisurePinpointWeather mb10"]/thead/tr/td/div/p/text()').extract()
		item['body2'] = sel.xpath('//table[@class="leisurePinpointWeather"]/thead/tr/td/div/p/text()').extract()
		item['kion'] = sel.xpath('//tr[@class="temperature"]/td/span/text()').extract()
		item['shitsudo'] = sel.xpath('//tr[@class="humidity"]/td/span/text()').extract()
		item['shitsudo2'] = sel.xpath('//tr[@class="humidity"]/td/text()').extract()
		
		yield item

	
