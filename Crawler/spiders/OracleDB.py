import scrapy
from scrapy.selector import Selector
from Crawler.spiders.Wiki_Spider import Wiki_Spider
from scrapy.utils.project import get_project_settings

class OracleLinuxSpider(Wiki_Spider):
    name = "oracledb"
    settings = get_project_settings()
    start_urls = [
        settings['URLS']['ORACLEDB']
    ]


    # def parse(self, response):

    #     items = response.xpath('//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr').getall()
    #     del items[0]
    #     result = dict()
    #     for item in items:
    #         version = Selector(text=item).xpath('.//td[1]/@data-sort-value').get()
    #         if version:
    #             result['Version'] = version.strip()
    #             date = Selector(text=item).xpath('.//td[3]/text()').get().strip()
    #             date_split = date.split(" ")
    #             if len(date_split) > 2:
    #                 date = date_split[0] + " " + date_split[1]
    #             result['Date'] = date
    #             yield result
            
