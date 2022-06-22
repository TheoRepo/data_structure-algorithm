#!/usr/bin/python
# -*- encoding: utf-8 -*-
#@File    :   search.py
#@Time    :   2022/06/17 08:16:18
#@Author  :   Theo Yu

import sys 
sys.path.append("..") 
from utils.cal_time import cal_time

# 线性查找
# 算法复杂度：O(n)
@cal_time
def linear_search(li, val):
    for ind, v in enumerate(li):
        if v == val:
            return ind
    else:
        return None

# 二分法查找
# 算法复杂度：O(log(n))
@cal_time
def binary_search(li, val):
    left = 0
    right = len(li) - 1
    while left <= right: # 候选区有值
        mid = (left + right) // 2
        if li[mid] == val:
            return mid
        elif li[mid] > val: # 待查找的值在mid左侧
            right = mid -1
        else: # li[mid] < val 带查找的值在mid右侧
            left = mid + 1
    else:
        return None


if __name__ == "__main__":
    li = list(range(10000))
    linear_search(li, 3890)
    binary_search(li, 3890)