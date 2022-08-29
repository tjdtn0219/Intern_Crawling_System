import scrapy
from scrapy.selector import Selector
import re
from scrapy.utils.project import get_project_settings
from Crawler.Funcs import Funcs

class InformixSpider(scrapy.Spider):
    name = "informix"
    settings = get_project_settings()
    start_urls = [
        settings['URLS']['INFORMIX']
    ]

    def parse(self, response):
        table_rows = response.xpath('//*[@id="system"]/article/table/tbody/tr').getall()
        del table_rows[0]

        result=dict()
        for row in table_rows:
            name = Selector(text=row).xpath('.//td[1]/strong/a/text()').get()
            version = Selector(text=row).xpath('.//td[2]/text()').get()
            version = re.sub(r'[^0-9.]', '', str(version)).rstrip('.')
            date = Selector(text=row).xpath('.//td[3]/text()').get()
                        
            if int(version.split('.')[0]) > 10:
                print(name + " "+version)
                print(date)
                result['Version'] = name + " " + version
                result['Date'] = Funcs.date_to_str(date)
                yield result