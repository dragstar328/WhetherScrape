# -*- coding: utf-8 -*-
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http.request import Request
from WhetherScrape.items import WhetherscrapeItem
from scrapy.selector import Selector

class TenkiJpSpieder(BaseSpider):
	name = "TenkiJp"
	allowed_domains = ["tenki.jp"]
	start_urls = [
		"http://www.tenki.jp/forecast/5/26/5110/23100-1hour.html"
	]
	
	def parse(self, response):
		item = WhetherscrapeItem()
		sel = Selector(response)
		
		item['body'] = response.xpath('//table[@class="leisurePinpointWeather mb10"]/thead/tr/td/div/p/text()').extract()
		item['body2'] = response.xpath('//table[@class="leisurePinpointWeather"]/thead/tr/td/div/p/text()').extract()
		item['jikoku'] = response.xpath('//tr[@class="hour"]').extract()
		item['kion'] = response.xpath('//tr[@class="temperature"]').extract()
		item['shitsudo'] = response.xpath('//tr[@class="humidity"]').extract()
		
		
		yield item

	
