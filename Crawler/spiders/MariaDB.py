import scrapy
from scrapy.selector import Selector
from Crawler.spiders.test_inherit import SpiderTest

class MariaDBpider(SpiderTest):
    name = "mariadb"
    start_urls = [
        'https://en.wikipedia.org/wiki/MariaDB',
    ]

    # def parse(self, response):
    #     table_rows = response.xpath('//*[@id="mw-content-text"]/div[1]/table[3]/tbody/tr').getall()
    #     del table_rows[0]
    #     del table_rows[-1]

    #     result = dict()
    #     for row in table_rows:
    #         name = Selector(text=row).xpath('.//td[1]/text()').get().strip()
    #         if name == "":
    #             name = Selector(text=row).xpath('.//td[1]/b/text()').get().strip()
    #         result['Version'] = name
    #         result['Date'] = Selector(text=row).xpath('.//td[4]/text()').get()
    #         yield result