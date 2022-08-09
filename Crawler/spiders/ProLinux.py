import scrapy
from scrapy.selector import Selector

class ProLinuxSpider(scrapy.Spider):
    name = "prolinux"
    start_urls = [
        'https://technet.tmaxsoft.com/ko/front/download/findDownloadList.do?cmProductCode=0702',
    ]

    def parse(self, response):
        items = response.xpath('//*[@id="article"]/article/div[3]/div').getall()
        result = dict()

        for item in items:
            version = Selector(text=item).xpath('.//div/table/thead/tr/th/text()').get().strip()
            if version:
                result['Version'] = version
                yield result
           