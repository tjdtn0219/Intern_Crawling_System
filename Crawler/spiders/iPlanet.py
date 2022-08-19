import scrapy
from scrapy.selector import Selector
from Crawler.spiders.Wiki_Spider import Wiki_Spider
from scrapy.utils.project import get_project_settings

class iPlanetSpider(Wiki_Spider):
    name = "iplanet"
    settings = get_project_settings()
    start_urls = [
        settings['URLS']['IPLANET']
    ]

    # def parse(self, response):
    #     items = response.xpath('//*[@id="mw-content-text"]/div[1]/ul[1]/li/text()').getall()

    #     result = dict()

    #     for item in items:
    #         result['Version'] = item.strip()
    #         yield result        