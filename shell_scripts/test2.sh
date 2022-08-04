#! /bin/bash

Scapy_CMD="scrapy crawl"
Project_Path="/var/lib/jenkins/Projects/LSSWARE_Crawler"
FILE_PATH="/var/lib/jenkins/Projects/LSSWARE_Crawler/new_output/"


LIST_OS_NAME="
windows
solaris
aix
hpux
redhat
centos
oraclelinux
suse
prolinux
cisco
alteon
avaya
critix
juniper
f5
extreme
oracledb
mssql
db2
sybase
sybaseiq
tibero
mysql
mariadb
altibase
cubrid
postgressql
informix
apache
ohs
iplanet
iis
nginx
webtob
weblogic
websphere
jeus
tomcat
jboss
jbossews
resin
"
LIST_OS_FAIL="

"

#Initial
cd ${Project_Path}
mkdir new_output ; cd new_output

#LOOP
for OS_NAME in $LIST_OS_NAME; do
    for i in {1..5}; do
        timeout 1m bash -c "${Scapy_CMD} ${OS_NAME} -O ${File_path}${OS_NAME}.json" \
        && \
        if [ -s "${OS_NAME}.json" ]; then 
            echo "${OS_NAME} : SUCCESS $i"
            break
        else
            FAIL_OS_FAIL+=${OS_NAME}
        fi
    done \
done \
&& \
echo "|=============================================================================|"
echo "|=============================================================================|"
echo "|===========================Complete Shell Scipt!=============================|"
echo "|=============================================================================|"
echo "|=============================================================================|"
if ((${#arr[@]})); then
    echo "|FAIL LIST : =================================================================|"
    for OS_NAME in $LIST_OS_FAIL; do
    echo "|=====${OS_NAME}"
fi
echo "|=============================================================================|"
echo "|=============================================================================|"
