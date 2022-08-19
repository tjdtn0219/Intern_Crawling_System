import scrapy
from scrapy.selector import Selector
from scrapy.utils.project import get_project_settings

class Cisco(scrapy.Spider):
    name = "cisco"
    settings = get_project_settings()
    start_urls = [
        settings['URLS']['CISCO']
    ]

    def parse(self, response):
        items = response.xpath('//*[@id="fw-content"]/div[2]/div[2]/div[2]/ul/li/span/text()').getall()

        result=dict()
        for item in items:
            # print(item.strip())
            if item.strip():
                result['Version']=item.strip()
                yield result
        