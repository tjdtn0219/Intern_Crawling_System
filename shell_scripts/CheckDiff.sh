#! /bin/bash

Project_Path="/var/lib/jenkins/Projects/LSSWARE_Crawler_v1/"

#Initial
cd ${Project_Path}

#Compare origin and new datas
while read OS_NAME; do
    if [ "${OS_NAME}" == "==END==" ]
    then
        break
    else
        IS_DIFF=$(diff ori_data/${OS_NAME}.json new_data/${OS_NAME}.json)
        if [ "$IS_DIFF" != "" ]
        then
            echo "${OS_NAME}" >> List_Diff.txt
        fi
    fi
done < ${Project_Path}List_OS.txt