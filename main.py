# -*- coding = utf-8 -*-
import os
from bs4 import BeautifulSoup #网页解析 获取数据
import urllib.request, urllib.error
import re    #正则表达式 文字匹配
import sqlite3 #存数据库
import xlwt
import sys


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')

def askURL(url):
    head ={
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 99.0.4844.51 Safari / 537.36 Edg / 99.0.1150.39"
    }
import time
t_param=time.time()
t_list=str(t_param).split(".") #将时间戳格式拆分
t_list[1][:3] #这是下划线前面的部分
t_list[1][3:]   #这是下划线后面的部分

# https://detail.tmall.com/item.htm?itemId=663154942834&sellerId=2838892713
