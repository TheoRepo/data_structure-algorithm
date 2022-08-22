#!/usr/bin/python
# -*- encoding: utf-8 -*-
#@File    :   cal_time.py
#@Time    :   2022/06/17 08:16:52
#@Author  :   Theo Yu


import time

def cal_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print("%s running time: %s secs." % (func.__name__, t2 - t1))
        return result
    return wrapper

