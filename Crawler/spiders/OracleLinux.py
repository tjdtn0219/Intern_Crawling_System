import scrapy
from scrapy.selector import Selector

class OracleLinuxSpider(scrapy.Spider):
    name = "oraclelinux"
    start_urls = [
        'https://en.wikipedia.org/wiki/Oracle_Linux',
    ]


    def parse(self, response):

        items = response.xpath('//*[@id="mw-content-text"]/div[1]/table[3]/tbody/tr').getall()
        del items[0]
        result = dict()
        for item in items:
            rspan=Selector(text=item).xpath('.//td[1]/@rowspan').get()
            if rspan:
                result['Name'] = Selector(text=item).xpath('.//th[1]/text()').get().strip()
                result['Date'] = Selector(text=item).xpath('.//td[3]/text()').get().strip()
                yield result
            else:
                version = result['Name'] = Selector(text=item).xpath('.//th[1]/text()').get()
                if version:
                    result['Name'] = version.strip()
                    result['Date'] = Selector(text=item).xpath('.//td[2]/text()').get().strip()
                    yield result
        
