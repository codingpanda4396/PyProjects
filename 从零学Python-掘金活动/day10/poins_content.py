#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Requests获取掘金沸点内容
author: gxcuizy
date: 2018-10-24
"""

import requests


def get_poins(url):
    """获取掘金沸点数据"""
    request = requests.get(url)
    result = request.json()
    return result


if __name__ == '__main__':
    poins_url = ''
    poins_result = get_poins(poins_url)
    poin_list = poins_result['d']['list']
    print('开始写入沸点内容……')
    with open('poins.txt', 'w', encoding='utf-8') as file:
        for poin in poin_list:
            user_name = poin['user']['username']
            print('写入【%s】发布的沸点……' % user_name)
            content = poin['content']
            file.write('沸点用户：' + user_name + '\n')
            file.write(content + '\n\n')
            file.write('************************************************************************************************************************' + '\n\n')
            print('写入完成！')
    print('全部写入完成！')
