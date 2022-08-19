#! /bin/bash

Project_Path="/var/lib/jenkins/Projects/LSSWARE_Crawler/"
Data_Path="/var/lib/jenkins/Projects/LSSWARE_Crawler/new_data1/"

#Initial
cd ${Project_Path}

#Check if datas are scraped suitably
while read OS_NAME; do
    if [ "${OS_NAME}" == "==END==" ]
    then
        break
    else
        if ! [ -s "${Data_Path}${OS_NAME}.json" ]
        then
            echo "${OS_NAME}"
            echo "${OS_NAME}" >> List_Fail.txt
        fi
    fi
done < ${Project_Path}List_OS.txt


