import scrapy
from scrapy.selector import Selector
from Crawler.spiders.Wiki_Spider import Wiki_Spider

class AIXSpider(Wiki_Spider):
    name = "aix"
    start_urls = [
        'https://en.wikipedia.org/wiki/IBM_AIX',
    ]
    def set_xpath(self):
        Wiki_Spider.xpath = "qqw"
    
    # def parse(self, response):
    #     release = ReleaseItem()
    #     items = response.xpath('//*[@id="mw-content-text"]/div[1]/table[4]/tbody/tr').getall()
    #     for item in items:
    #         if Selector(text=item).xpath('.//td/@data-sort-value').get():
    #             release['Version'] = Selector(text=item).xpath('.//td/@data-sort-value').get().strip()
    #             date = Selector(text=item).xpath('.//td[2]/text()').get().strip()
    #             release['Date'] = date.replace('\u00a0', " ")
    #             yield release

