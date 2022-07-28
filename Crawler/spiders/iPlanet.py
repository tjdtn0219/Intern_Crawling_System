import scrapy
from scrapy.selector import Selector

class iPlanetSpider(scrapy.Spider):
    name = "iplanet"
    start_urls = [
        'https://en.wikipedia.org/wiki/Oracle_iPlanet_Web_Server',
    ]

    def parse(self, response):
        items = response.xpath('//*[@id="mw-content-text"]/div[1]/ul[1]/li/text()').getall()

        result = dict()

        for item in items:
            result['Name'] = item.strip()
            yield result        