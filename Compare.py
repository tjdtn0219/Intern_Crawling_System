import json
from DateFormat import Change_Date_Format, compare_others
from datetime import datetime

path = "/var/lib/jenkins/Projects/LSSWARE_Crawler/"


def Read_File(file_name):
    list = []
    with open(path + file_name + ".txt", "r") as file:
        list=[]
        lines = file.readlines()
        for line in lines:
            list.append(line.rstrip())
        return list

def Read_Json(file_name, type):
    list_order = Read_File("List_Order")
    list_json = []
    if type == "new":
        with open(path + "new_data/" + file_name+ ".json") as json_f:
            data = json.load(json_f)
            list_json = data
               
    elif type == "ori":
        with open(path + "ori_data/" + file_name+ ".json") as json_f:
            data = json.load(json_f)
            list_json = data
    
    if file_name in list_order:
        #This is for unifying all json to descending order
        list_json = list(reversed(list_json))

    return list_json

def Write_File(list_alert):
    with open(path + "email_message.txt", "w") as file:
        for item in list_alert:
            file.write("#" + item['Name'] + "\n")
            file.write(item['Date'] + " : " + item['Version'] + " 버전이 릴리즈 되었습니다.\n\n")


def compare(ori_data, new_data, os_name):
    if "Date" in ori_data[0]:
        ori_date = Change_Date_Format(ori_data[0]["Date"])
        new_date = Change_Date_Format(new_data[0]["Date"])
        if ori_date < new_date:
            #Alert New Release
            new_data[0]['Name'] = os_name
            return new_data[0]
            pass
    else:
        result = dict()
        result['Name'] = os_name
        result['Version'] = new_data[0]["Version"]
        result['Date'] = str(datetime.now().date())
        return result
        #Compare ori
        

#===============================================================#
list_diff = Read_File("List_Diff")
list_alert = []

for os_name in list_diff:
    print(os_name.strip())
    ori_data = Read_Json(os_name.strip(), "ori")
    new_data = Read_Json(os_name.strip(), "new")

    if os_name == "extreme" or os_name == "informix":
        #extrme, informix json can not be ordered by asc nor desc
        list_alert += compare_others(ori_data, new_data, os_name)
        pass
    else:
        if compare(ori_data, new_data, os_name):
            list_alert.append(compare(ori_data, new_data, os_name))

if len(list_alert) > 0:
    Write_File(list_alert)
    

