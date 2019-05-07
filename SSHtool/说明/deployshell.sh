#!/usr/bin/env bash
#！/bin/bash
#不是脚本，未测试的deploy command on controll node
OS='ubuntu 18.04'
openstack='rocky'
user='root'
role='controll node'
#--------------------------------------------------------------------#
#可选 NTP 
apt install chrony
#replace NTP_SERVER with hostname or ip in /etc/chrony/chrony.conf
server NTP_SERVER iburst
#add other node
allow 10.0.0.1/24
#restart NTP SERVER
service chrony restart

#--------------------------------------------------------------------#
#1)OpenStack packages
#Enable the repository for Ubuntu Cloud Archive
add-apt-repository cloud-archive:rocky
#Upgrade packages
apt update && apt dist-upgrade
#Install the OpenStack client
apt install python-openstackclient

#--------------------------------------------------------------------#
#2)SQL database for Ubuntu
#Install the packages
apt install mysql-server python-pymysql