#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
http://www.zkh360.com/zkh_cathlog/3.html
翻页网址不变化，需要找到真实请求
分析-测试-重复
https://www.zhihu.com/people/excited-vczh/following 提取vczh关注者信息
问题：
谷歌浏览器网页源代码+json无法显示
'''

import requests
import pandas as pd

url = "https://www.zhihu.com/api/v4/members/excited-vczh/followees?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=20&limit=20"

headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}

response = requests.get(url,headers=headers).json()['data'] # 获取字典的值
#print(type(response))  # 字典类型
#print(response)

# 保存数据
df = pd.DataFrame.from_dict(response) # 来自字典，默认文本类型text
#print(df.head)
df.to_csv("/Users/Young/Desktop/zhihu.csv") # 保存csv