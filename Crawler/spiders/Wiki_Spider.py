import scrapy
from scrapy.selector import Selector
from Crawler.items import ReleaseItem
from Crawler.Wiki_Funcs import ScrapyFuncs

class Wiki_Spider(scrapy.Spider):

    def parse(self, response):
        Break = ReleaseItem()
        Break['Version'] = "BREAK_LINE"
        Break['Date'] = "BREAK_LINE"
        tables_sources = response.xpath('//table[contains(@class, "wikitable")]').getall()

        tables = ScrapyFuncs.select_tables(tables_sources) #Find tables and select proper tables
        
        if len(tables) == 0:
            # scrapy from catalog, which is not from tables
            for item in ScrapyFuncs.parsing_catalog(response):
                yield item
            pass
        else:
            # scrapy from tables
            for table in tables:
                for item in ScrapyFuncs.parsing_table(table):
                    yield item
                yield Break
            pass
                
            
