import scrapy
from scrapy.selector import Selector

class IIS_Spider(scrapy.Spider):
    name = "iis"
    start_urls = [
        'https://docs.microsoft.com/en-us/lifecycle/products/internet-information-services-iis',
    ]

    def parse(self, response):
        table_rows = response.xpath('//*[@id="main"]/div[3]/div/section[2]/table/tbody/tr').getall()

        result = dict()

        for row in table_rows:
            result['Version'] = Selector(text=row).xpath('.//td[1]/text()').get().strip()
            result['Date'] = Selector(text=row).xpath('.//td[2]/local-time/text()').get().strip().split('T')[0]
            yield result