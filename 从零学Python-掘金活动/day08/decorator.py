#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
装饰器的使用-判断素数
author: gxcuizy
date: 2018-10-22
"""

import functools


def decorator_prime(prime_func_name):
    """装饰器的使用"""

    @functools.wraps(prime_func_name)
    def before(number):
        """前置输出信息"""
        print('%s 是不是素数？' % number)
        return prime_func_name(number)

    return before


@decorator_prime
def is_prime(number):
    """判断一个数是否为素数"""
    if number < 2:
        return False
    # 中间整数
    number_center = int(number / 2)
    # 最小数只能为2以上
    start = 2
    # 是否为素数
    prime_status = True
    # 循环整除中间数以下的数字
    while start <= number_center:
        if number % start == 0:
            prime_status = False
            break
        start += 1
    return prime_status


# 程序主入口
if __name__ == '__main__':
    while True:
        # 接收一个整数
        input_number = input('请输入一个整数（输入q退出）：')
        if input_number == 'q':
            break
        # 素数判断结果
        result = is_prime(int(input_number))
        # 打印输出
        if result:
            print(input_number + '是素数')
        else:
            print(input_number + '不是素数')
