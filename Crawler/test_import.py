
from scrapy.selector import Selector
from Crawler.items import ReleaseItem

class TestClass:
    def listToString(str_list):
        result = ""
        for s in str_list:
            result += s + " "
        return result.strip()

    def isStrEmpty(str):
        if str is None:
            return False
        
        else:
            if str.strip() == "":
                return False
            else:
                return True

    def parsing_version_in_row(table_row, version_col_idx):
            
        idx = version_col_idx[0] + 1
        if TestClass.isStrEmpty(Selector(text=table_row).xpath('.//tr/*[' + str(idx) + ']/text()').get()):
            version = Selector(text=table_row).xpath('.//tr/*[' + str(idx) + ']/text()').get().strip()
        elif TestClass.isStrEmpty(Selector(text=table_row).xpath('.//tr/*[' + str(idx) + ']/a/text()').get()):
            version = Selector(text=table_row).xpath('.//tr/*[' + str(idx) + ']/a/text()').get().strip()
        elif TestClass.isStrEmpty(Selector(text=table_row).xpath('.//tr/*[' + str(idx) + ']/@data-sort-value').get()):
            version = Selector(text=table_row).xpath('.//tr/*[' + str(idx) + ']/@data-sort-value').get().strip()
        else:
            version = None
        
        return version

    def parsing_date_in_row(table_row, date_col_idx, rowspan_is_flag, rowspan_flag):
        if rowspan_is_flag:
            if rowspan_flag:
                idx = date_col_idx[0] + 1
            else:
                idx = date_col_idx[0]
        else:
            idx = date_col_idx[0] + 1
            
        if TestClass.isStrEmpty(Selector(text=table_row).xpath('.//tr/*[' + str(idx) + ']/text()').get()):
            date = Selector(text=table_row).xpath('.//tr/*[' + str(idx) + ']/text()').get().strip()
        else:
            date = None
            if len(date_col_idx) > 1:
                if TestClass.isStrEmpty(Selector(text=table_row).xpath('.//tr/*[' + str(idx) + ']/text()').get()):
                    date = Selector(text=table_row).xpath('.//tr/*[' + str(idx) + ']/text()').get().strip()

        return date

    def find_col_idx(table_heads, str_list):
        col_idx = []
        for i, head in enumerate(table_heads):
            head_list = Selector(text=head).xpath('.//text()').getall()
            head = TestClass.listToString(head_list)
            # print(head)
            for str in str_list:
                if str in head.lower():
                    col_idx.append(i)

        return col_idx

    def delete_table_heads(table_rows):                
        while len(Selector(text=table_rows[0]).xpath('.//td').getall()) == 0:
            del table_rows[0]


        