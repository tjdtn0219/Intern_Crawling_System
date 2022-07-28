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
            if Selector(text=item).xpath('.//div/table/tbody/tr[2]/th/ul/li[2]/text()').get().strip():  #8.1~
                result['Name'] = Selector(text=item).xpath('.//div/table/tbody/tr[2]/th/ul/li[2]/text()').get().strip('보안패치').strip()
                yield result
            else:   #Version 7 Table
                table_items = Selector(text=item).xpath('.//table/tbody/tr/th/ul/li[3]/text()').getall()
                for table_item in table_items:
                    if "보안패치" in table_item:
                        pass
                    else:
                        result['Name'] = table_item.strip()
                        # result['Date'] = 
                        yield result
        