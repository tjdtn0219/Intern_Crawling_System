import scrapy
from scrapy.selector import Selector
from Crawler.spiders.Wiki_Spider import Wiki_Spider
from scrapy.utils.project import get_project_settings

class MySQLpider(Wiki_Spider):
    name = "mysql"
    settings = get_project_settings()
    start_urls = [
        settings['URLS']['MYSQL']
    ]

    # def parse(self, response):
    #     table_rows = response.xpath('//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr').getall()
    #     del table_rows[0]

    #     result = dict()
    #     for row in table_rows:
    #         result['Version'] = Selector(text=row).xpath('.//th/@data-sort-value').get()
    #         result['Date'] = Selector(text=row).xpath('.//td[3]/text()').get().strip()
    #         yield result