import scrapy
from scrapy.selector import Selector
import re
from Crawler.spiders.Wiki_Spider import Wiki_Spider

class SUSESpider(Wiki_Spider):
    name = "suse"
    start_urls = [
        'https://en.wikipedia.org/wiki/SUSE_Linux',
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
                
