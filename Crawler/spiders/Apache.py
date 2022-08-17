import scrapy
from scrapy.selector import Selector
from Crawler.spiders.test_inherit import SpiderTest

class ApacheSpider(SpiderTest):
    name = "apache"
    start_urls = [
        'https://en.wikipedia.org/wiki/Apache_HTTP_Server',
    ]

    # def parse(self, response):
    #     table_rows = response.xpath('//*[@id="mw-content-text"]/div[1]/table[3]/tbody/tr').getall()
    #     del table_rows[0]

    #     result=dict()
    #     for row in table_rows:
    #         version = Selector(text=row).xpath('.//th/text()').get()
    #         if version and version != " ":
    #             result['Version'] = version.strip()
    #         else:
    #             version = result['Name'] = Selector(text=row).xpath('.//th/b/text()').get()
    #             if version:
    #                 result['Version'] = version
    #         result['Date'] = Selector(text=row).xpath('.//td[1]/text()').get()

    #         if version:
    #             yield result