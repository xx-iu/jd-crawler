# -*- coding = utf-8 -*-
# @Time : 2022/5/14 17:27
# @Author : xuxiang
# @File : jd.py

import requests
import re

'''
https://club.jd.com/comment/productPageComments.action?
callback=fetchJSON_comment98
&productId=1233203
&score=0
&sortType=5
&page=1
&pageSize=10
&isShadowSku=0
&fold=1
'''


def main():
    first = 1
    for i in range(1, 50):
        url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=1233203&score=0&sortType=5&pageSize=10&isShadowSku=0&fold=1&page='
        finalurl = url + str(i) + '&pageSize=10&isShadowSku=0&fold=1'

        header = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
                  }
        data = requests.get(url=finalurl,headers=header).text
        remodel_comment = re.compile(r'\"content\":\"([^"]+)\",\"(?:creationTime|vcontent)\"')  # 匹配评论
        comment_list = remodel_comment.findall(data)

        for i in comment_list:
            print(first,":",i)
            first += 1

main()
