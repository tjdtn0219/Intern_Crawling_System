import scrapy
from scrapy.selector import Selector

class HPUXSpider(scrapy.Spider):
    name = "hpux"
    start_urls = [
        'https://en.wikipedia.org/wiki/HP-UX',
    ]


    def parse(self, response):
        
        items = response.xpath('//*[@id="mw-content-text"]/div[1]/table[6]/tbody/tr').getall()
        result = dict()
        for item in items:
            if Selector(text=item).xpath('.//td').get():
                result['Version'] = Selector(text=item).xpath('.//td/@data-sort-value').get().strip()
                # if Selector(text=item.xpath('.//td[2]'))
                result['Date'] = Selector(text=item).xpath('.//td[2]/text()').get().strip()
                yield result
