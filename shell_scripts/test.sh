#! /bin/bash

Scapy_CMD="scrapy crawl"
Project_Path="/var/lib/jenkins/Projects/LSSWARE_Crawler_v1"
FILE_PATH="/var/lib/jenkins/Projects/LSSWARE_Crawler_v1/new_output/"

#OS
File_Windows=${FILE_PATH}Windows.json
File_Solaris=${FILE_PATH}Solaris.json
File_AIX=${FILE_PATH}AIX.json
File_HP_UX=${FILE_PATH}HP_UX.json
File_RedHat=${FILE_PATH}RedHat.json
File_CentOS=${FILE_PATH}CentOS.json
File_OracleLinux=${FILE_PATH}OracleLinux.json
File_SUSE=${FILE_PATH}SUSE.json
File_ProLinux=${FILE_PATH}ProLinux.json

#Network
File_Cisco=${FILE_PATH}Cisco.json
File_Alteon=${FILE_PATH}Alteon.json
File_Avaya=${FILE_PATH}Avaya.json
File_Critix=${FILE_PATH}Critix.json
File_Juniper=${FILE_PATH}Juniper.json
File_F5=${FILE_PATH}F5.json
File_Extreme=${FILE_PATH}Extreme.json

#DBMS
File_OracleDB=${FILE_PATH}OracleDB.json
File_MSSQL=${FILE_PATH}MSSQL.json
File_DB2=${FILE_PATH}DB2.json
File_Sybase=${FILE_PATH}Sybase.json
File_SybaseIQ=${FILE_PATH}SybaseIQ.json
File_Tibero=${FILE_PATH}Tibero.json
File_MySQL=${FILE_PATH}MySQL.json
File_MariaDB=${FILE_PATH}MariaDB.json
File_Altibase=${FILE_PATH}Altibase.json
File_CUBRID=${FILE_PATH}CUBRID.json
File_PostgresSQL=${FILE_PATH}PosgresSQL.json
File_Informix=${FILE_PATH}Informix.json

#WEBWAS
File_Apache=${FILE_PATH}Apache.json
File_OHS=${FILE_PATH}OHS.json
File_iPlanet=${FILE_PATH}iPlanet.json
File_IIS=${FILE_PATH}IIS.json
File_Nginx=${FILE_PATH}Nginx.json
File_WebToB=${FILE_PATH}WebToB.json
File_WebLogic=${FILE_PATH}WebLogic.json
File_WebSphere=${FILE_PATH}WebShpere.json
File_JEUS=${FILE_PATH}JEUS.json
File_Tomcat=${FILE_PATH}Tomcat.json
File_JBOSS=${FILE_PATH}JBOSS.json
File_JBOSS_EWS=${FILE_PATH}JBOSS_EWS.json
File_Resin=${FILE_PATH}Resin.json
###

#Initial
cd ${Project_Path}

#Windows
for i in {1..5}
do
    ${Scapy_CMD} windows -O ${File_Windows} \
    && \
    if [ -s "$File_Windows" ]
    then 
        echo "Alteon : SUCCESS $i"
        break
    fi
done \
&& \
#Solaris
for i in {1..5}
do
    ${Scapy_CMD} solaris -O ${File_Solaris} \
    && \
    if [ -s "$File_Solaris" ]; then 
        echo "Solaris : SUCCESS $i"
        break
    fi
done \
&& \
#AIX
for i in {1..5}
do
    ${Scapy_CMD} aix -O ${File_AIX} \
    && \
    if [ -s "$File_AIX" ]; then 
        echo "AIX : SUCCESS $i"
        break
    fi
done \
&& \
#HP_UX
for i in {1..5}
do
    ${Scapy_CMD} hpux -O ${File_HP_UX} \
    && \
    if [ -s "$File_HP_UX" ]; then 
        echo "HP_UX : SUCCESS $i"
        break
    fi
done \
&& \
#RedHat
for i in {1..5}
do
    ${Scapy_CMD} redhat -O ${File_RedHat} \
    && \
    if [ -s "$File_RedHat" ]; then 
        echo "RedHat : SUCCESS $i"
        break
    fi
done \
&& \
#CentOS
for i in {1..5}
do
    ${Scapy_CMD} centos -O ${File_CentOS} \
    && \
    if [ -s "$File_CentOS" ]; then 
        echo "CentOS : SUCCESS $i"
        break
    fi
done \
&& \
#OracleLinux
for i in {1..5}
do
    ${Scapy_CMD} oraclelinux -O ${File_OracleLinux} \
    && \
    if [ -s "$File_OracleLinux" ]; then 
        echo "OracleLinux : SUCCESS $i"
        break
    fi
done \
&& \
#SUSE
for i in {1..5}
do
    ${Scapy_CMD} suse -O ${File_SUSE} \
    && \
    if [ -s "$File_SUSE" ]; then 
        echo "SUSE : SUCCESS $i"
        break
    fi
done \
&& \
#ProLinux
for i in {1..5}
do
    ${Scapy_CMD} prolinux -O ${File_ProLinux} \
    && \
    if [ -s "$File_ProLinux" ]; then 
        echo "ProLinux : SUCCESS $i"
        break
    fi
done \
&& \
#Cisco
for i in {1..5}
do
    ${Scapy_CMD} cisco -O ${File_Cisco} \
    && \
    if [ -s "$File_Cisco" ]; then 
        echo "Cisco : SUCCESS $i"
        break
    fi
done \
&& \
#Alteon
for i in {1..5}
do
    ${Scapy_CMD} alteon -O ${File_Alteon} \
    && \
    if [ -s "$File_Alteon" ]; then 
        echo "Alteon : SUCCESS $i"
        break
    fi
done \
&& \
#Avaya
for i in {1..5}
do
    ${Scapy_CMD} avaya -O ${File_Avaya} \
    && \
    if [ -s "$File_Avaya" ]; then 
        echo "Avaya : SUCCESS $i"
        break
    fi
done \
&& \
#Critix
for i in {1..5}
do
    ${Scapy_CMD} critix -O ${File_Critix} \
    && \
    if [ -s "$File_Critix" ]; then 
        echo "Critix : SUCCESS $i"
        break
    fi
done \
&& \
#Juniper
for i in {1..5}
do
    ${Scapy_CMD} juniper -O ${File_Juniper} \
    && \
    if [ -s "$File_Juniper" ]; then 
        echo "Juniper : SUCCESS $i"
        break
    fi
done \
&& \
#F5
for i in {1..5}
do
    ${Scapy_CMD} f5 -O ${File_F5} \
    && \
    if [ -s "$File_F5" ]; then 
        echo "F5 : SUCCESS $i"
        break
    fi
done \
&& \
#Extreme
for i in {1..5}
do
    ${Scapy_CMD} extreme -O ${File_Extreme} \
    && \
    if [ -s "$File_HP_UX" ]; then 
        echo "Extreme : SUCCESS $i"
        break
    fi
done \
&& \
#OracleDB
for i in {1..5}
do
    ${Scapy_CMD} oracledb -O ${File_OracleDB} \
    && \
    if [ -s "$File_OracleDB" ]; then 
        echo "OracleDB : SUCCESS $i"
        break
    fi
done \
&& \
#MSSQL
for i in {1..5}
do
    ${Scapy_CMD} mssql -O ${File_MSSQL} \
    && \
    if [ -s "$File_MSSQL" ]; then 
        echo "MSSQL : SUCCESS $i"
        break
    fi
done \
&& \
#DB2
for i in {1..5}
do
    ${Scapy_CMD} db2 -O ${File_DB2} \
    && \
    if [ -s "$File_DB2" ]; then 
        echo "DB2 : SUCCESS $i"
        break
    fi
done \
&& \
#Sybase
for i in {1..5}
do
    ${Scapy_CMD} sybase -O ${File_Sybase} \
    && \
    if [ -s "$File_Sybase" ]; then 
        echo "Sybase : SUCCESS $i"
        break
    fi
done \
&& \
#SybaseIQ
for i in {1..5}
do
    ${Scapy_CMD} sybaseiq -O ${File_SybaseIQ} \
    && \
    if [ -s "$File_SybaseIQ" ]; then 
        echo "SybaseIQ : SUCCESS $i"
        break
    fi
done \
&& \
#Tibero
for i in {1..5}
do
    ${Scapy_CMD} tibero -O ${File_Tibero} \
    && \
    if [ -s "$File_Tibero" ]; then 
        echo "Tibero : SUCCESS $i"
        break
    fi
done \
&& \
#MySQL
for i in {1..5}
do
    ${Scapy_CMD} mysql -O ${File_MySQL} \
    && \
    if [ -s "$File_MySQL" ]; then 
        echo "MySQL : SUCCESS $i"
        break
    fi
done \
&& \
#MariaDB
for i in {1..5}
do
    ${Scapy_CMD} mariadb -O ${File_MariaDB} \
    && \
    if [ -s "$File_MariaDB" ]; then 
        echo "MairaDB : SUCCESS $i"
        break
    fi
done \
&& \
#Altibase
for i in {1..5}
do
    ${Scapy_CMD} altibase -O ${File_Altibase} \
    && \
    if [ -s "$File_Altibase" ]; then 
        echo "Altibase : SUCCESS $i"
        break
    fi
done \
&& \
#CUBRID
for i in {1..5}
do
    ${Scapy_CMD} cubrid -O ${File_CUBRID} \
    && \
    if [ -s "$File_CUBRID" ]; then 
        echo "CUBRID : SUCCESS $i"
        break
    fi
done \
&& \
#PostgresSQL
for i in {1..5}
do
    ${Scapy_CMD} postgressql -O ${File_PostgresSQL} \
    && \
    if [ -s "$File_PostgresSQL" ]; then 
        echo "PostgresSQL : SUCCESS $i"
        break
    fi
done \
&& \
#Informix
for i in {1..5}
do
    ${Scapy_CMD} informix -O ${File_Informix} \
    && \
    if [ -s "$File_Informix" ]; then 
        echo "Informix : SUCCESS $i"
        break
    fi
done \
&& \
#Apache
for i in {1..5}
do
    ${Scapy_CMD} apache -O ${File_Apache} \
    && \
    if [ -s "$File_Apache" ]; then 
        echo "Apache : SUCCESS $i"
        break
    fi
done \
&& \
#OHS
for i in {1..5}
do
    ${Scapy_CMD} informix -O ${File_OHS} \
    && \
    if [ -s "$File_OHS" ]; then 
        echo "OHS : SUCCESS $i"
        break
    fi
done \
&& \
#iPlanet
for i in {1..5}
do
    ${Scapy_CMD} informix -O ${File_iPlanet} \
    && \
    if [ -s "$File_iPlanet" ]; then 
        echo "iPlanet : SUCCESS $i"
        break
    fi
done \
&& \
#IIS
for i in {1..5}
do
    ${Scapy_CMD} iis -O ${File_IIS} \
    && \
    if [ -s "$File_IIS" ]; then 
        echo "IIS : SUCCESS $i"
        break
    fi
done \
&& \
#Nginx
for i in {1..5}
do
    ${Scapy_CMD} nginx -O ${File_Nginx} \
    && \
    if [ -s "$File_Nginx" ]; then 
        echo "Nginx : SUCCESS $i"
        break
    fi
done \
&& \
#WebToB
for i in {1..5}
do
    ${Scapy_CMD} webtob -O ${File_WebToB} \
    && \
    if [ -s "$File_WebToB" ]; then 
        echo "WebToB : SUCCESS $i"
        break
    fi
done \
&& \
#WebLogic
for i in {1..5}
do
    ${Scapy_CMD} weblogic -O ${File_WebLogic} \
    && \
    if [ -s "$File_WebLogic" ]; then 
        echo "WebLogic : SUCCESS $i"
        break
    fi
done \
&& \
#WebSphere
for i in {1..5}
do
    ${Scapy_CMD} websphere -O ${File_WebSphere} \
    && \
    if [ -s "$File_WebSphere" ]; then 
        echo "WebSphere : SUCCESS $i"
        break
    fi
done \
&& \
#JEUS
for i in {1..5}
do
    ${Scapy_CMD} jeus -O ${File_JEUS} \
    && \
    if [ -s "$File_JEUS" ]; then 
        echo "JEUS : SUCCESS $i"
        break
    fi
done \
&& \
#Tomcat
for i in {1..5}
do
    ${Scapy_CMD} tomcat -O ${File_Tomcat} \
    && \
    if [ -s "$File_Tomcat" ]; then 
        echo "Tomcat : SUCCESS $i"
        break
    fi
done \
&& \
#JBOSS
for i in {1..5}
do
    ${Scapy_CMD} jboss -O ${File_JBOSS} \
    && \
    if [ -s "$File_JBOSS" ]; then 
        echo "JBOSS : SUCCESS $i"
        break
    fi
done \
&& \
#JBOSS_EWS
for i in {1..5}
do
    ${Scapy_CMD} jbossews -O ${File_JBOSS_EWS} \
    && \
    if [ -s "$File_JBOSS_EWS" ]; then 
        echo "JBOSS_EWS : SUCCESS $i"
        break
    fi
done \
&& \
#Resin
for i in {1..5}
do
    ${Scapy_CMD} resin -O ${File_Resin} \
    && \
    if [ -s "$File_Resin" ]; then 
        echo "Resin : SUCCESS $i"
        break
    fi
done \
&&
echo "===================================="
echo "=======Complete Shell Scipt!========"
echo "===================================="