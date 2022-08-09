import json
from datetime import datetime

def Change_Date_Format(str_date):
    list_formats = [
        "%B %d, %Y", "%d %B %Y", "%Y-%m-%d", "%B %Y", "%Y/%m/%d", "%b %Y", "%d/%m/%Y",
        "%m/%d/%Y"
    ]
    for format in list_formats:
        try:
            date_obj = datetime.strptime(str_date, format)
            return date_obj

        except ValueError:
            continue
    
def compare_extreme_informix(ori_data, new_data, os_name):
    print("---")
    ori_max = Change_Date_Format(ori_data[0]['Date']).date()
    for data in ori_data:
        date = Change_Date_Format(data['Date']).date()
        if ori_max < date:
            ori_max = date
    print("ori_max : ")
    print(ori_max)
    list = []
    for data in new_data:
        if ori_max < Change_Date_Format(data['Date']).date():
            data['Name'] = os_name
            list.append(data)
    return list