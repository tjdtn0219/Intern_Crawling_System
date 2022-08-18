import scrapy
from scrapy.selector import Selector
from Crawler.spiders.Wiki_Spider import Wiki_Spider

class CUBRIDSpider(Wiki_Spider):
    name = "cubrid"
    start_urls = [
        'https://en.wikipedia.org/wiki/CUBRID',
    ]

    # def parse(self, response):
    #     table_rows = response.xpath('//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr').getall()
    #     del table_rows[0]

    #     result=dict()
    #     for row in table_rows:
    #         result['Version'] = Selector(text=row).xpath('.//th/text()').get().strip()
    #         result['Date'] = Selector(text=row).xpath('.//td[1]/text()').get().strip()
    #         yield result