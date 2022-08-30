#! /bin/bash

Scapy_CMD="scrapy crawl"
Project_Path="/var/lib/jenkins/Projects/LSSWARE_Crawler_v1/"
FILE_PATH="/var/lib/jenkins/Projects/LSSWARE_Crawler_v1/new_data/"

LIST_OS_RETRY=()

#Initial
cd ${Project_Path}
source .venv/bin/activate && \
mkdir ${FILE_PATH} ; cd ${FILE_PATH}

#LOOP
while read OS_NAME; do
    if [ "${OS_NAME}" == "==END==" ]
    then
        break
    else
        echo ${OS_NAME}
        for i in {1..2}; do
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
done < ${Project_Path}$1\
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
    echo "|=========================ALL SPIDERS SCRAPY SUCCESSED!=======================|"
fi
echo "|=============================================================================|"
echo "|=============================================================================|"