#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Requests的练习和使用
author: gxcuizy
date: 2018-10-20
"""

import requests

# 程序主入口
if __name__ == '__main__':
    # 请求URL
    url = 'https://www.baidu.com/'

    request = requests.get(url)

    # 请求状态
    status_code = request.status_code
    print(request.status_code)

    # 请求的文本字符串
    request_text = request.text
    print(request_text)

    # 使用content属性获得bytes对象
    request_content = request.content
    print(request_content)

    # 使用json()直接获取JSON数据类型
    request_json = request.json()
    print(request_json)

    # 发送POST请求使用requests.post(url, data={})
    # 同理，put()、delete()等请求也是的

    # 需要传入HTTP Header时，需要传入一个dict作为headers参数
    # header = {
    #     'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
    # }
    # request = requests.get(url, headers=header)
    # # 打印结果
    # print(request.json())

    # # 需要传cookie的话，也是传一个cookies的dict字典

    # # 要指定超时，传入以秒为单位的timeout参数
    # request = requests.get(url, headers=header, timeout=3)
    # # 打印结果
    # print(request.json())
