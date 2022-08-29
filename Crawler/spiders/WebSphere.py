import scrapy
from scrapy.selector import Selector
import re
from scrapy.utils.project import get_project_settings
from Crawler.Funcs import Funcs

class WebLogicSpider(scrapy.Spider):
    name = "websphere"
    settings = get_project_settings()
    start_urls = [
        settings['URLS']['WEBSPHERE']
    ]


    def parse(self, response):
        
        version_list = response.xpath('//*[@id="mw-content-text"]/div[1]/table[3]/tbody/tr[1]/td/text()').getall()
        del version_list[0]

        date_list = response.xpath('//*[@id="mw-content-text"]/div[1]/table[3]/tbody/tr[3]/td/text()').getall()
        date_list.remove('\n')
        del date_list[0]

        result = dict()

        if len(version_list) == len(date_list):
            for i in range(len(version_list)):
                result['Version'] = version_list[i].strip()
                result['Date'] = Funcs.date_to_str(date_list[i].strip())
                yield result
                