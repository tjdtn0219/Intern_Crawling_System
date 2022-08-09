import scrapy
from scrapy.selector import Selector

class Cisco(scrapy.Spider):
    name = "cisco"
    start_urls = [
        'https://www.cisco.com/c/ko_kr/support/ios-nx-os-software/index.html#allDevices',
    ]

    def parse(self, response):
        items = response.xpath('//*[@id="fw-content"]/div[2]/div[2]/div[2]/ul/li/span/text()').getall()

        result=dict()
        for item in items:
            # print(item.strip())
            if item.strip():
                result['Version']=item.strip()
                yield result
        