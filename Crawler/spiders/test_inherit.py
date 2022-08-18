import scrapy
from scrapy.selector import Selector
from Crawler.items import ReleaseItem
from Crawler.test_import import TestClass

class SpiderTest(scrapy.Spider):
    xpath = ""
    Version_heads = ["version", "name", "release", "series", "general availability"]
    Date_heads = ["first release", "release date", "date of issue", "latest release"]
            

    def set_xpath(self):
        SpiderTest.xpath = "dd"

    def parse(self, response):
        release = ReleaseItem()
        release['Version'] = "BREAK_LINE"
        release['Date'] = "BREAK_LINE"
        tables_sources = response.xpath('//table[contains(@class, "wikitable")]').getall()

        tables = TestClass.select_tables(tables_sources)
        
        if len(tables) == 0:
            # scrapy from catalog, not from tables
            print("======================")
            print("d")
            for item in TestClass.parsing_catalog(response):
                yield item
            pass
        else:
            # scrapy from tables
            for table in tables:
                for item in TestClass.parsing_table(table):
                    yield item
                yield release
                
            
