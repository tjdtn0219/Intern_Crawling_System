import scrapy
from scrapy.selector import Selector
from Crawler.spiders.Wiki_Spider import Wiki_Spider
from scrapy.utils.project import get_project_settings

class HPUXSpider(Wiki_Spider):
    name = "hpux"
    settings = get_project_settings()
    start_urls = [
        settings['URLS']['HP_UX']
    ]


    # def parse(self, response):
        
    #     items = response.xpath('//*[@id="mw-content-text"]/div[1]/table[6]/tbody/tr').getall()
    #     result = dict()
    #     for item in items:
    #         if Selector(text=item).xpath('.//td').get():
    #             result['Version'] = Selector(text=item).xpath('.//td/@data-sort-value').get().strip()
    #             # if Selector(text=item.xpath('.//td[2]'))
    #             # result['Date'] = Selector(text=item).xpath('.//td[2]/text()').get().strip()
    #             yield result
