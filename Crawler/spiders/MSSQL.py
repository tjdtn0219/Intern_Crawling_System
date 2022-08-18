import scrapy
from scrapy.selector import Selector
from Crawler.spiders.Wiki_Spider import Wiki_Spider


class OracleLinuxSpider(Wiki_Spider):
    name = "mssql"
    start_urls = [
        'https://en.wikipedia.org/wiki/History_of_Microsoft_SQL_Server#SQL_Server_2017',
    ]


    # def parse(self, response):
    #     items = response.xpath('//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr').getall()
    #     del items[0]
    #     result = dict()
    #     for item in items:
    #         version = Selector(text=item).xpath('.//td[1]/text()').get().strip()
    #         if version != "":
    #             result['Version'] = version.strip()
    #             yield result
    #         else:
    #             result['Version'] = Selector(text=item).xpath('.//td[1]/a/text()').get().strip()
    #             yield result
