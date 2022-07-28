import scrapy
from scrapy.selector import Selector

class RedhatSpider(scrapy.Spider):
    name = "redhat"
    start_urls = [
        'https://en.wikipedia.org/wiki/Red_Hat_Enterprise_Linux',
    ]


    def parse(self, response):
        
        items = response.xpath('//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr').getall()
        result = dict()
        for item in items:
            if Selector(text=item).xpath('.//td').get():
                result['Version'] = Selector(text=item).xpath('.//td/@data-sort-value').get().strip()
                result['Date'] = Selector(text=item).xpath('.//td[2]/text()').get().strip()
                yield result
            
