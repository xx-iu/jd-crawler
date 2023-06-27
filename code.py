# -*- coding = utf-8 -*-
# @Time : 2022/3/16 11:47
# @Author : xuxiang
# @File : code.py

import time
import requests
import csv
import json
import os
import random


class taobaoSpider_content():
    # """通过分析网址的Ajax获取淘宝商品评论
    # 其中get_page方法是构造出url并且返回json格式的文本数据,get_content
    # 方法用于提取数据并返回一个生成器，最后main方法整合输出结果
    # Attributes: itemId:商品ID
    # Attributes：currentPage:评论页码
    # Attributes：sellerId:淘宝商家Id
    # """

    def __init__(self, itemId, sellerId, currentPage):
        self.currentPage = currentPage
        self.url = "https://rate.tmall.com/list_detail_rate.htm?"
        self.headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39",
        "referer": "https://detail.tmall.com/item.htm",
        "Cookie": 'cna=ASJgGlsjp1UCAbfmDLxSbMu1; cdpid=UU6nQPA%2FMWTqoA%3D%3D; cnaui=2661837177; aui=2661837177; sca=ab3e0232; tbsa=2fadae26ca817a17377686d2_1647413679_2; atpsida=69a0a1e43579ca6f0804a08c_1647414665_4'
        }
        self.itemId = itemId
        self.sellerId = sellerId


    def get_page(self):
        t_param = time.time()
        t_list = str(t_param).split(".")
        params = {"sellerId": self.sellerId,
                  "itemId": self.itemId,
                  "callback": str(int(t_list[1][3:]) + 1),
                  "_ksTS": t_list[0] + t_list[1][:3] + "_" + t_list[1][3:],
                  "currentPage": self.currentPage
                  }
        res = requests.get(self.url, params=params, headers=self.headers)
        try:
            if res.status_code == 200:
                res = requests.get(self.url, params=params, headers=self.headers).text[len(t_list[1][3:]) + 3:-1]
                res_json = json.loads(res)
                res_str = json.dumps(res_json, indent=4)
                return json.loads(res_str)
        except:
            return None


    def get_content(self, json_data):
        if json_data != None:
            for item in json_data.get("rateDetail").get("rateList"):
                content_time = item.get("rateDate")
                content_type = item.get("auctionSku")
                content_name = item.get("displayUserNick")
                content_data = item.get("rateContent")
                yield {
                    "content_time": content_time,
                    "content_type": content_type,
                    "content_name": content_name,
                    "content_data": content_data,
                }
        else:
            print("该页出错啦！")
            return None


    def write_txt(self, data):
        # """这是将结果写入txt文本文档的格式
        #
        #    将字典写入文本文档首先要利用json.dumps()转换成字符串格式.
        #    json.dumps的indent参数是为了美化输出
        #    json.ensure_ascii参数将数据输出程中文，同时要规定文件输出编码为utf-8
        # """
        with open("taobaocontent2.txt", "a", encoding="utf-8") as file:
            file.write(json.dumps(data, indent=2, ensure_ascii=False))
            file.write("\n")


    def write_csv(self, data):
        # """这是将结果写入csv文件
        #    将字典直接写入csv需要用到csv模块。具体可以参考相关文档
        #    这里要注意写入csv容易出现中文乱码，需要加encoding和newline参数。
        # """


        with open("taobaocontent2.csv", "a", encoding="utf-8-sig", newline='') as file:
            fieldnames = ["content_time", "content_type", "content_name", "content_data"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(data)


    def main(self):
        json_data = self.get_page()
        self.get_content(json_data)
        return self.get_content(json_data)


if __name__ == "__main__":
    for i in range(1, 2):
        new_data = taobaoSpider_content(itemId=654955060692, sellerId=1917047079, currentPage=i)
    if new_data.main() != None:
        for items in new_data.main():
            new_data.write_txt(items)
    else:
        pass
    time.sleep(random.randint(5, 10))  # 设置延时防止爬虫被封
