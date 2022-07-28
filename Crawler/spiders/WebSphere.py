import scrapy
from scrapy.selector import Selector
import re
class WebLogicSpider(scrapy.Spider):
    name = "websphere"

    start_urls = [
        'https://en.wikipedia.org/wiki/IBM_WebSphere_Application_Server',
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
                result['Name'] = version_list[i].strip()
                result['Date'] = date_list[i].strip()
                yield result
                