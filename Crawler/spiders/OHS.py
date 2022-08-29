import scrapy
from scrapy.selector import Selector
from scrapy.utils.project import get_project_settings

class OHSSpider(scrapy.Spider):
    name = "ohs"
    settings = get_project_settings()
    start_urls = [
        settings['URLS']['OHS']
    ]


    def parse(self, response):
        items = response.xpath('/html/body/div/section[2]/div/table/tbody/tr/td/div/a/text()').getall()
        
        result = dict()

        for item in items:
            result['Version'] = item.strip()
            result['Date'] = None
            yield result