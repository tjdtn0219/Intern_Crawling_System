import scrapy
from scrapy.selector import Selector
from Crawler.spiders.Timax_Spider import Timax_Spider
from scrapy.utils.project import get_project_settings

class ProLinuxSpider(Timax_Spider):
    name = "prolinux"
    settings = get_project_settings()
    start_urls = [
        settings['URLS']['PROLINUX']
    ]

    # def parse(self, response):
    #     items = response.xpath('//*[@id="article"]/article/div[3]/div').getall()
    #     result = dict()

    #     for item in items:
    #         version = Selector(text=item).xpath('.//div/table/thead/tr/th/text()').get().strip()
    #         if version:
    #             result['Version'] = version
    #             yield result
           