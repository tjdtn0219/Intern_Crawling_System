import scrapy
from scrapy.selector import Selector

class TomcatSpider(scrapy.Spider):
    name = "tomcat"
    start_urls = [
        'https://en.wikipedia.org/wiki/Apache_Tomcat',
    ]


    def parse(self, response):
        table_rows = response.xpath('//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr').getall()
        del table_rows[0]
        del table_rows[0]
        del table_rows[-1]

        result = dict()
        for row in table_rows:
            version = Selector(text=row).xpath('.//td[1]/@data-sort-value').get().strip()
            date = Selector(text=row).xpath('.//td[5]/text()').get().strip()
            result['Name'] = version
            result['Date'] = date
            yield result