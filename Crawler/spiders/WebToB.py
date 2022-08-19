import scrapy
from scrapy.selector import Selector
from Crawler.spiders.Timax_Spider import Timax_Spider
from scrapy.utils.project import get_project_settings

class WebToBSpider(Timax_Spider):
    name = "webtob"
    settings = get_project_settings()
    start_urls = [
        settings['URLS']['WEBTOB']
    ]


    # def parse(self, response):
    #     tables = response.xpath('/html/body/div[2]/div[2]/div/div[2]/article/div[3]/div').getall()
    #     del tables[0]

        # result = dict()
        # for table in tables:
        #     items = Selector(text=table).xpath('.//table/tbody/tr/th/ul/li[3]/text()').getall()
        #     for item in items:
        #         result['Version'] = item.strip()
        #         yield result