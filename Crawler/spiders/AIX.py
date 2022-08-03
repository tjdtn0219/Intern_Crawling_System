import scrapy
from scrapy.selector import Selector

class AIXSpider(scrapy.Spider):
    name = "aix"
    start_urls = [
        'https://en.wikipedia.org/wiki/IBM_AIX',
    ]

    def parse(self, response):

        items = response.xpath('//*[@id="mw-content-text"]/div[1]/table[4]/tbody/tr').getall()
        result = dict()
        for item in items:
            if Selector(text=item).xpath('.//td/@data-sort-value').get():
                result['Version'] = Selector(text=item).xpath('.//td/@data-sort-value').get().strip()
                result['Date'] = Selector(text=item).xpath('.//td[2]/text()').get().strip()
                yield result
