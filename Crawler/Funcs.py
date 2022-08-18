
from scrapy.selector import Selector
from Crawler.items import ReleaseItem
from datetime import datetime

class Funcs:
    Version_heads = ["version", "name", "release", "series", "general availability"]
    Date_heads = ["first release", "release date", "date of issue", "latest release"]
    list_formats = [
            "%B %d, %Y", "%d %B %Y", "%Y-%m-%d", "%B %Y", "%Y/%m/%d", "%b %Y", "%d/%m/%Y",
            "%m/%d/%Y", "%Y.%m", "%B\u00a0%d, %Y", "%d\u00a0%B %Y", "%Y"
        ]

    def listToString(str_list):
        result = ""
        for s in str_list:
            result += s.strip() + " "
        return result.strip()

    def isStrEmpty(str):
        if str is None:
            return False
        
        else:
            if str.strip() == "":
                return False
            else:
                return True

    def date_to_str(str_date):
        for format in Funcs.list_formats:
            try:
                date_obj = datetime.strptime(str_date, format)
                return date_obj.strftime("%Y/%m/%d")

            except ValueError:
                continue
        return None
