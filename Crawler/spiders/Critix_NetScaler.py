import scrapy
from scrapy.selector import Selector
from scrapy.utils.project import get_project_settings

class Critix_NetScalerSpider(scrapy.Spider):
    name = 'critix'
    settings = get_project_settings()
    start_urls = [
        settings['URLS']['CRITIX']
    ]


    def parse(self, response):
        items = response.xpath('/html/body/div/div/div[2]/div[3]/div[2]/div/div[1]/div/div/h2/text()').getall()
        result = dict()
        for item in items:
            string = item.strip()
            if string:
                result['Version'] = string
                yield result

                