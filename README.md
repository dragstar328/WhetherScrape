# WhetherScrape
Scrape from website  
http://www.tenki.jp/forecast/5/26/5110/23100-1hour.html

## usage
scrapy crawl TenkiJp -o output.json  
rm *.json && scrapy crawl TenkiJp -o output.json

## Todo
- ~~analyze json~~
- insert(update) db
- crowl automatically
- use pipeline
