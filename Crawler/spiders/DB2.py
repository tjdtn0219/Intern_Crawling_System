import scrapy
from scrapy.selector import Selector
from Crawler.spiders.Wiki_Spider import Wiki_Spider

class DB2Spider(Wiki_Spider):
    name = "db2"
    start_urls = [
        'https://en.wikipedia.org/wiki/IBM_Db2',
    ]


    # def parse(self, response):
    #     items = response.xpath('//*[@id="mw-content-text"]/div[1]/ul[7]/li').getall()
    #     del items[0]
    #     result = dict()
    #     for item in items:
    #         version = Selector(text=item).xpath('.//li/text()').get().strip()
    #         result['Version'] = version.strip()
    #         yield result