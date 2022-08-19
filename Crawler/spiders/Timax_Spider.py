import scrapy
from scrapy.selector import Selector
from Crawler.items import ReleaseItem
from Crawler.Funcs import Funcs

class Timax_Spider(scrapy.Spider):

    def parse(self, response):
        release = ReleaseItem()
        Break = ReleaseItem()
        Break['Version'] = "BREAK_LINE"
        Break['Date'] = "BREAK_LINE"
        items = response.xpath('//tr[@class="tr_tit"]/th/text()').getall()

        for item in items:
            if item:
                item = item.strip()
                item_split = item.split(" ")
                if len(item_split) > 1:
                    if Funcs.str_to_float(item_split[1]):
                        release['Version'] = item
                        release['Date'] = None
                        yield release


                
            
