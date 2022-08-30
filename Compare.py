import json
from datetime import datetime
from Crawler.Funcs import Funcs

path = "/var/lib/jenkins/Projects/LSSWARE_Crawler_v1/"


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
    ###This is write new releases information on the email text###
    with open(path + "email_message.txt", "w") as file:
        for item in list_alert:
            file.write("#" + item['Name'] + "\n")
            file.write(item['Date'] + " : " + item['Version'] + " 버전이 릴리즈 되었습니다.\n\n")


def compare(ori_data, new_data, os_name):
    ###This is to compare ori_data with new_data except exdtreme and informix###
    temp_ori_data = []
    temp_new_data = []
    temp_ori_data.append([])
    temp_new_data.append([])

    ###Divide into each table###
    j=0
    for i, item in enumerate(ori_data):
        if ori_data[i]['Version'] == "BREAK_LINE":
            if i > 0:
                temp_ori_data.append([])
                j += 1
            continue

        temp_dict = dict()
        temp_dict['Version'] = ori_data[i]['Version']
        temp_dict['Date'] = ori_data[i]['Date']
        temp_ori_data[j].append(temp_dict)
    
        i += 1

    j=0
    for i, item in enumerate(new_data):
        if new_data[i]['Version'] == "BREAK_LINE":
            if i > 0:
                temp_new_data.append([])
                j += 1
            continue

        temp_dict = dict()
        temp_dict['Version'] = new_data[i]['Version']
        temp_dict['Date'] = new_data[i]['Date']
        temp_new_data[j].append(temp_dict)

        i += 1
    ###Divide into each table###

    ###This is a policy for comparing (If you want to modify the policy, modify under codes)###
    assert len(temp_ori_data) == len(temp_new_data)
    result = []
    item = dict()
    for i in range(len(temp_ori_data)):
        if len(temp_ori_data[i]) < len(temp_new_data[i]):
            if temp_new_data[i][0]["Date"]:
                item['Name'] = os_name
                item['Version'] = temp_new_data[i][0]['Version']
                item['Date'] = temp_new_data[i][0]['Date']
            else:
                item['Name'] = os_name
                item['Version'] = temp_new_data[i][0]['Version']
                item['Date'] = str(datetime.now().date())
            result.append(item)
    return result

def compare_others(ori_data, new_data, os_name):
    ###This is only for extreme and informix####
    ori_max = Funcs.str_to_date((ori_data[0]['Date']))
    for data in ori_data:
        date = Funcs.str_to_date((data['Date']))
        if ori_max < date:
            ori_max = date
    list = []
    for data in new_data:
        if ori_max < Funcs.str_to_date((data['Date'])):
            data['Name'] = os_name
            list.append(data)
    return list

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
        list_alert += compare(ori_data, new_data, os_name)

if len(list_alert) > 0:
    Write_File(list_alert)
    

