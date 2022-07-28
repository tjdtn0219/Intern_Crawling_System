import scrapy
from scrapy.selector import Selector

class AvayaSpider(scrapy.Spider):
    name = 'avaya'

    start_urls = [
        'https://www.devconnectprogram.com/site/global/products_resources/avaya_aura_communication_manager/releases/10_1/index.gsp',
    ]

    def parse(self, response):
        items = response.xpath('//*[@id="overview"]/div[2]/div').getall()
        result = dict()
        for item in items:
            values = Selector(text=item).xpath('.//ul/li/a/text()').getall()
            for value in values:
                value = value.strip()
                strings = value.split(' ', maxsplit=1)
                result['Name'] = strings[0].strip()
                result['Date'] = strings[1].strip("() ")
                yield result

                