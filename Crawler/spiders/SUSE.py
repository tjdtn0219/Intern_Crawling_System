import scrapy
from scrapy.selector import Selector
import re
from Crawler.spiders.Wiki_Spider import Wiki_Spider
from scrapy.utils.project import get_project_settings

class SUSESpider(Wiki_Spider):
    name = "suse"
    settings = get_project_settings()
    start_urls = [
        settings['URLS']['SUSE']
    ]


    # def parse(self, response):
    #     items = response.xpath('//*[@id="mw-content-text"]/div[1]/table[5]/tbody/tr').getall()
    #     result = dict()
    #     for item in items:
    #         version_value = Selector(text=item).xpath('.//td[1]/@data-sort-value').get()
    #         version_value = re.sub(r'[^0-9.]', '', str(version_value))
    #         if version_value:
    #             result['Version'] = version_value
    #             result['Date'] = Selector(text=item).xpath('.//td[3]/text()').get().strip()
    #             yield result
                
