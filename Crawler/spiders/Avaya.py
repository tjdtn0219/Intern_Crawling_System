import scrapy
from scrapy.selector import Selector
from scrapy.utils.project import get_project_settings
from Crawler.Funcs import Funcs

class AvayaSpider(scrapy.Spider):
    name = 'avaya'
    settings = get_project_settings()
    start_urls = [
        settings['URLS']['AVAYA']
    ]

    def parse(self, response):
        items = response.xpath('//*[@id="overview"]/div[2]/div').getall()
        result = dict()
        for item in items:
            values = Selector(text=item).xpath('.//ul/li/a/text()').getall()
            for value in values:
                value = value.strip()
                strings = value.split(' ', maxsplit=1)
                result['Version'] = strings[0].strip()
                result['Date'] = Funcs.date_to_str(strings[1].strip("() "))
                yield result

                