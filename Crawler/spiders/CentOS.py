import scrapy
from scrapy.selector import Selector
from Crawler.spiders.Wiki_Spider import Wiki_Spider

class RedhatSpider(Wiki_Spider):
    name = "centos"
    start_urls = [
        'https://en.wikipedia.org/wiki/CentOS',
    ]


    # def parse(self, response):
    #     #//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr[1]
    #     items = response.xpath('//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr').getall()
    #     result = dict()
    #     for item in items:
    #         if Selector(text=item).xpath('.//th/@data-sort-value').get():
    #             result['Version'] = Selector(text=item).xpath('.//th/@data-sort-value').get().strip()
    #             result['Date'] = Selector(text=item).xpath('.//td[1]/text()').get().strip()
    #             yield result
            
