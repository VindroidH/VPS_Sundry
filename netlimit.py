#!/usr/bin/python
#coding:utf-8
'''
author:ningci dev
date:2017-04-30 05:54
此python 脚本检测网卡流量使用情况，当达到设定值时，就会使用 iptables 关闭 80 443 
'''
import time
import os
import re
import string
import subprocess

#每天限制流量使用15.5G~
DAY_LIMIT_OF_MB = 16000

class NetLimit:

    def __net_up(self):
        os.system("iptables -A INPUT -p tcp --dport 8080 -j ACCEPT")
        os.system("iptables -A OUTPUT -p tcp --dport 8080 -j ACCEPT")

    def __net_down(self):
        os.system("iptables -A INPUT -p tcp --dport 8080 -j REJECT")
        os.system("iptables -A OUTPUT -p tcp --dport 8080 -j REJECT")

    def __check_flow(self):
        vnstat_days = subprocess.check_output(["vnstat", "-i", "eth0", "-d"])
        #使用正则匹配每行匹配当前日期
        vnstat_rows = re.findall(r"([\d|/]{10})\s+([\w\.\s]+)[^\d]+([\w\.\s]+)[^\d]+([\w\.\s]+)", vnstat_days)
        #输出格式 [('01/01/2018', '10.00 MiB ', '10.00 MiB ', '20.00 MiB '), ('01/02/2018', '10.00 MiB ', '20.00 MiB ', '30.00 MiB ')]
        for vnstat_row in vnstat_rows:
            #比较当前日期
            if time.strftime("%m/%d/%Y", time.localtime(time.time())) == vnstat_row[0]:
                total_day = vnstat_row[3]
                #查询 流量单位 MiB , KiB 忽略不计
                if 0 < total_day.find("MiB"):
                    #果然是不如 PHP 方便，PHP 可以直接转为 int 
                    #使用 空格拆分取数字
                    total_day = string.atof(total_day.split(" ")[0])
                    if total_day > DAY_LIMIT_OF_MB:
                        return True
        return False
    
    def __init__(self):
        self.__net_up()

    def run(self):
            self.__net_down() if self.__check_flow() else self.__net_up()

NetLimit().run()