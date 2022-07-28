import scrapy
from scrapy.selector import Selector

class OracleLinuxSpider(scrapy.Spider):
    name = "oracledb"
    start_urls = [
        'https://en.wikipedia.org/wiki/Oracle_Database',
    ]


    def parse(self, response):

        items = response.xpath('//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr').getall()
        del items[0]
        result = dict()
        for item in items:
            version = Selector(text=item).xpath('.//td[1]/@data-sort-value').get()
            if version:
                result['Name'] = version.strip()
                result['Date'] = Selector(text=item).xpath('.//td[3]/text()').get().strip()
                yield result
            
