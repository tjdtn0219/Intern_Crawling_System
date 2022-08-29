import scrapy
from scrapy.selector import Selector
from scrapy.utils.project import get_project_settings

class NginxSpider(scrapy.Spider):
    name = "nginx"
    settings = get_project_settings()
    start_urls = [
        settings['URLS']['NGINX']
    ]


    def parse(self, response):
        items = response.xpath('//*[@id="content"]/table/tr/td[2]/a[1]/text()').getall()
        
        result = dict()

        for item in items:
            result['Version'] = item.strip()
            result['Date'] = None
            yield result