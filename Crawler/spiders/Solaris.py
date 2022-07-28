import scrapy
from scrapy.selector import Selector

class SolarisSpider(scrapy.Spider):
    name = "solaris"
    start_urls = [
        'https://en.wikipedia.org/wiki/Oracle_Solaris',
    ]

    def parse(self, response):
        items = response.xpath('//*[@id="mw-content-text"]/div[1]/table[3]/tbody/tr').getall()
        result = dict()
        for item in items:
            if Selector(text=item).xpath('.//td').get():
                result['Version'] = Selector(text=item).xpath('.//td/@data-sort-value').get()
                result['Date'] = Selector(text=item).xpath('.//td[3]/text()').get().strip()
                yield result
