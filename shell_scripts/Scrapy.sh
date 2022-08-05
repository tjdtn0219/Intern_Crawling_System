#! /bin/bash

Scapy_CMD="scrapy crawl"
Project_Path="/var/lib/jenkins/Projects/LSSWARE_Crawler/"
FILE_PATH="/var/lib/jenkins/Projects/LSSWARE_Crawler/new_data/"

LIST_OS_RETRY=()

#Initial
cd ${Project_Path}
source .venv/bin/activate && \
mkdir new_data ; cd new_data

#LOOP
while read OS_NAME; do
    if [ "${OS_NAME}" == "==END==" ]
    then
        break
    else
        echo ${OS_NAME}
        for i in {1..50}; do
        timeout 2m bash -c "${Scapy_CMD} ${OS_NAME} -O ${File_path}${OS_NAME}.json" \
        && \
        if [ -s "${OS_NAME}.json" ]
        then 
            echo "=========${OS_NAME} : SUCCESS $i========="
            break
        else
            echo "===========RETRY : ${i}==========="
            LIST_OS_RETRY+=("${OS_NAME}")
            sleep 5s
        fi
    done
    fi
done < ${Project_Path}OS_List.txt\
&& \
echo "|=============================================================================|"
echo "|=============================================================================|"
echo "|===========================Complete Shell Scipt!=============================|"
echo "|=============================================================================|"
echo "|=============================================================================|"
if ((${#LIST_OS_RETRY[@]}))
then
    echo "|RETRY_LIST : ================================================================|"
    for OS_NAME in $LIST_OS_RETRY; do
        echo "|==============${OS_NAME} : Please Check if ${OS_NAME}.json file has datas."
    done
else
    echo "|==========================ALL SPIDERS SCRAPY SUCCESSED!=======================|"
fi
echo "|=============================================================================|"
echo "|=============================================================================|"