import scrapy
from scrapy.selector import Selector

class NginxSpider(scrapy.Spider):
    name = "nginx"
    start_urls = [
        'http://nginx.org/en/download.html',
    ]


    def parse(self, response):
        items = response.xpath('//*[@id="content"]/table/tr/td[2]/a[1]/text()').getall()
        
        result = dict()

        for item in items:
            result['Version'] = item.strip()
            yield result