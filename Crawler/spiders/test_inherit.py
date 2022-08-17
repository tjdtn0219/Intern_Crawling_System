import scrapy
from scrapy.selector import Selector
from Crawler.items import ReleaseItem
from Crawler.test_import import TestClass

class SpiderTest(scrapy.Spider):
    xpath = ""

    def set_xpath(self):
        SpiderTest.xpath = "dd"

    def parse(self, response):
        release = ReleaseItem()

        tables = response.xpath('//table[contains(@class, "wikitable")]').getall()

        print("===========len===========")
        print(len(tables))

        if len(tables) == 0:
            pass
        elif len(tables) == 1:
            table_rows = Selector(text=tables[0]).xpath('.//tbody/tr').getall()
            table_heads = Selector(text=table_rows[0]).xpath('.//th').getall()
            Version_heads = ["version", "name", "release", "series", "general availability"]
            Date_heads = ["first release", "release date", "date of issue", "latest release", "initial release"]
            
            version_col_idx = TestClass.find_col_idx(table_heads, Version_heads)
            date_col_idx = TestClass.find_col_idx(table_heads, Date_heads)
                
            TestClass.delete_table_heads(table_rows)
            
            # if Selector(text=table_rows[-1]).xpath('.//')

        else:
            pass

        rowspan_is_flag = False
        for table_row in table_rows:
            print("========================11")
            rowspan_flag = False
            if Selector(text=table_row).xpath('.//tr/*/@rowspan').get():
                rowspan_is_flag = True
                rowspan_flag = True

            version = TestClass.parsing_version_in_row(table_row, version_col_idx)
            date = TestClass.parsing_date_in_row(table_row, date_col_idx, rowspan_is_flag, rowspan_flag)

            if version is not None and date is not None: 
                release['Version'] = version
                release['Date'] = date
                # release['Date'] = date.replace('\u00a0', " ")
                yield release
