import scrapy
from scrapy.selector import Selector
from Crawler.spiders.Timax_Spider import Timax_Spider
from scrapy.utils.project import get_project_settings

class TiberoSpider(Timax_Spider):
    name = "tibero"
    settings = get_project_settings()
    start_urls = [
        settings['URLS']['TIBERO']
    ]

    # def parse(self, response):
    #     items = response.xpath('//*[@id="article"]/article/div[3]/div/table/thead/tr/th/text()').getall()

    #     result = dict()
    #     for item in items:
    #         if "Tibero" in item and "Studio" not in item:
    #             result['Version'] = item.strip()
    #             yield result