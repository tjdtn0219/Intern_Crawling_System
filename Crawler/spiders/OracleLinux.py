import scrapy
from scrapy.selector import Selector
from Crawler.spiders.Wiki_Spider import Wiki_Spider
from scrapy.utils.project import get_project_settings

class OracleLinuxSpider(Wiki_Spider):
    name = "oraclelinux"
    settings = get_project_settings()
    start_urls = [
        settings['URLS']['ORACLELINUX']
    ]


    # def parse(self, response):

    #     items = response.xpath('//*[@id="mw-content-text"]/div[1]/table[3]/tbody/tr').getall()
    #     del items[0]
    #     result = dict()
    #     for item in items:
    #         rspan=Selector(text=item).xpath('.//td[1]/@rowspan').get()
    #         if rspan:
    #             result['Version'] = Selector(text=item).xpath('.//th[1]/text()').get().strip()
    #             date = Selector(text=item).xpath('.//td[3]/text()').get().strip()
    #             if date == "?":
    #                 date = Selector(text=item).xpath('.//td[4]/text()').get().strip()
    #             result['Date'] = date
    #             yield result
    #         else:
    #             version = result['Version'] = Selector(text=item).xpath('.//th[1]/text()').get()
    #             if version:
    #                 result['Version'] = version.strip()
    #                 date = Selector(text=item).xpath('.//td[2]/text()').get().strip()
    #                 if date == "?":
    #                     date = Selector(text=item).xpath('.//td[3]/text()').get().strip()
    #                 result['Date'] = date
    #                 yield result
        
