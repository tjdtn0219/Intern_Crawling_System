import scrapy
from scrapy.selector import Selector
from Crawler.spiders.Wiki_Spider import Wiki_Spider
from scrapy.utils.project import get_project_settings

class RedhatSpider(Wiki_Spider):
    name = "redhat"
    settings = get_project_settings()
    start_urls = [
        settings['URLS']['REDHAT']
    ]


    # def parse(self, response):
        
    #     items = response.xpath('//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr').getall()
    #     result = dict()

    #     del items[-1]
    #     for item in items:
    #         if Selector(text=item).xpath('.//td').get():
    #             result['Version'] = Selector(text=item).xpath('.//td/@data-sort-value').get().strip()
    #             date = Selector(text=item).xpath('.//td[2]/text()').get().strip()
    #             date_split = date.split(" ")
    #             if len(date_split) == 4:
    #                 date = date_split[0] + " " + date_split[1] + " " + date_split[2]
    #             result['Date'] = date

    #             yield result
            
