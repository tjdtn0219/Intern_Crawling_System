import scrapy
from scrapy.selector import Selector
from Crawler.items import ReleaseItem
from Crawler.Scrapy_Funcs import ScrapyFuncs

class Wiki_Spider(scrapy.Spider):
    xpath = ""
    Version_heads = ["version", "name", "release", "series", "general availability"]
    Date_heads = ["first release", "release date", "date of issue", "latest release"]
            

    def set_xpath(self):
        Wiki_Spider.xpath = "dd"

    def parse(self, response):
        release = ReleaseItem()
        release['Version'] = "BREAK_LINE"
        release['Date'] = "BREAK_LINE"
        tables_sources = response.xpath('//table[contains(@class, "wikitable")]').getall()

        tables = ScrapyFuncs.select_tables(tables_sources)
        
        if len(tables) == 0:
            # scrapy from catalog, not from tables
            print("======================")
            print("d")
            for item in ScrapyFuncs.parsing_catalog(response):
                yield item
            pass
        else:
            # scrapy from tables
            for table in tables:
                for item in ScrapyFuncs.parsing_table(table):
                    yield item
                yield release
                
            
