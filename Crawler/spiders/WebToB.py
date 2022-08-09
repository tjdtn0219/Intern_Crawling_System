import scrapy
from scrapy.selector import Selector

class WebToBSpider(scrapy.Spider):
    name = "webtob"
    start_urls = [
        'https://technet.tmaxsoft.com/ko/front/download/findDownloadList.do?cmProductCode=0102',
    ]


    def parse(self, response):
        tables = response.xpath('/html/body/div[2]/div[2]/div/div[2]/article/div[3]/div').getall()
        del tables[0]

        result = dict()
        for table in tables:
            items = Selector(text=table).xpath('.//table/tbody/tr/th/ul/li[3]/text()').getall()
            for item in items:
                result['Version'] = item.strip()
                yield result