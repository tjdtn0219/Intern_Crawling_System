import scrapy
from scrapy.selector import Selector

class PostgresSQLSpider(scrapy.Spider):
    name = "postgressql"
    start_urls = [
        'https://en.wikipedia.org/wiki/PostgreSQL',
    ]

    def parse(self, response):
        table_rows = response.xpath('//*[@id="mw-content-text"]/div[1]/table[3]/tbody/tr').getall()
        del table_rows[0]

        result=dict()
        for row in table_rows:
            result['Version'] = Selector(text=row).xpath('.//th/text()').get().strip()
            date = Selector(text=row).xpath('.//td[1]/text()').get().strip()
            if "\u2014" not in date:
                result['Date'] = Selector(text=row).xpath('.//td[1]/text()').get().strip()
            else:
                result['Date'] = Selector(text=row).xpath('.//td[3]/text()').get().strip()
            # result['Name'] = Selector(text=row).xpath('.//td[2]/@data-sort-value').get().strip()
            # result['Date'] = Selector(text=row).xpath('.//td[3]/text()').get().strip() // latest version
            yield result