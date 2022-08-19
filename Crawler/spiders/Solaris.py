import scrapy
from scrapy.selector import Selector
from Crawler.spiders.Wiki_Spider import Wiki_Spider
from scrapy.utils.project import get_project_settings

class SolarisSpider(Wiki_Spider):
    name = "solaris"
    settings = get_project_settings()
    start_urls = [
        settings['URLS']['SOLARIS']
    ]

    # def parse(self, response):
    #     items = response.xpath('//*[@id="mw-content-text"]/div[1]/table[3]/tbody/tr').getall()
    #     result = dict()
    #     for item in items:
    #         if Selector(text=item).xpath('.//td').get():
    #             result['Version'] = Selector(text=item).xpath('.//td/@data-sort-value').get()
    #             date = Selector(text=item).xpath('.//td[3]/text()').get().strip()
    #             result['Date'] = date.replace("\u00a0", " ")
    #             yield result
