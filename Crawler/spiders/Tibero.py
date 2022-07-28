import scrapy
from scrapy.selector import Selector

class TiberoSpider(scrapy.Spider):
    name = "tibero"
    start_urls = [
        'https://technet.tmaxsoft.com/ko/front/download/findDownloadList.do?cmProductCode=0301',
    ]

    def parse(self, response):
        items = response.xpath('//*[@id="article"]/article/div[3]/div/table/thead/tr/th/text()').getall()

        result = dict()
        for item in items:
            if "Tibero" in item and "Studio" not in item:
                result['Name'] = item.strip()
                yield result