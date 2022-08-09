#! /bin/bash

Project_Path="/var/lib/jenkins/Projects/LSSWARE_Crawler/"

#Initial
cd ${Project_Path}

#ReScrapy
if [[ -f ${Project_Path}List_Fail.txt ]]
then
    ./shell_scripts/Scrapy.sh List_Fail.txt
else
    echo "List_Fail.txt does not exists"
fi



