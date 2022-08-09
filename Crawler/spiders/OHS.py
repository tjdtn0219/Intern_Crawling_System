import scrapy
from scrapy.selector import Selector

class OHSSpider(scrapy.Spider):
    name = "ohs"
    start_urls = [
        'https://www.oracle.com/kr/middleware/technologies/webtier-downloads.html',
    ]


    def parse(self, response):
        items = response.xpath('/html/body/div/section[2]/div/table/tbody/tr/td/div/a/text()').getall()
        
        result = dict()

        for item in items:
            result['Version'] = item.strip()
            yield result