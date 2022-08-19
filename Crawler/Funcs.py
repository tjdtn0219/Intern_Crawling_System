
from scrapy.selector import Selector
from Crawler.items import ReleaseItem
from datetime import datetime
from scrapy.utils.project import get_project_settings

class Funcs:
    settings = get_project_settings()
    Version_heads = settings['VERSION_HEADS']
    Date_heads = settings['DATE_HEADS']
    list_formats = settings['LIST_FORMATS']

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

    def str_to_float(str):
        try:
            f_val = float(str)
            return f_val
        except ValueError:
            return None
