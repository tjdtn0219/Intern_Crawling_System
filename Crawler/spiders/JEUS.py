import scrapy
from scrapy.selector import Selector

class JEUSSpider(scrapy.Spider):
    name = "jeus"
    start_urls = [
        'https://technet.tmaxsoft.com/ko/front/download/findDownloadList.do?cmProductCode=0101',
    ]


    def parse(self, response):
        tables = response.xpath('//*[@id="article"]/article/div[3]/div').getall()
        del tables[-1]
        del tables[0]

        result = dict()
        for table in tables:
            items = Selector(text=table).xpath('.//table/tbody/tr/th/ul/li/text()').getall()
            for item in items:
                if item.strip():
                    result['Name'] = item.strip()
                    yield result