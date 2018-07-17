#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
http://www.zkh360.com/zkh_cathlog/3.html
翻页网址不变化，需要找到真实请求
分析-测试-重复
https://www.zhihu.com/people/excited-vczh/following 提取vczh关注者信息
问题：
谷歌浏览器网页源代码+json无法显示

保存单网页：设置请求头-获取数据-保存数据
保存多网页：找到翻页变量-翻页函数-存储数据-爬取提升
'''

import requests
import pandas as pd
import time

headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}
user_data = []
def get_user_data(page):
    for i in range(page):
        url = "https://www.zhihu.com/api/v4/members/excited-vczh/followees" \
              "?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2C" \
              "follower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F" \
              "(type%3Dbest_answerer)%5D.topics&offset={}&limit=20".format(i * 20)

        response = requests.get(url,headers=headers).json()['data'] # 获取字典的值
        user_data.extend(response)
        print("正在爬取第%s页" % str(i+1))
        time.sleep(1)
        #print(type(response))  # 字典类型
        #print(response)
if __name__ == '__main__':
    get_user_data(10)
    # 保存数据
    df = pd.DataFrame.from_dict(user_data) # 来自字典，默认文本类型text
    #print(df.head)
    df.to_csv("/Users/Young/Desktop/zhihu.csv") # 保存csv