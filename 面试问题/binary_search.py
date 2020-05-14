#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :binary_search.py
@说明        :
@时间        :2020/05/04 14:24:31
@作者        :gbw
@版本        :1.0
'''


def binary_search1(arr=[], num=0):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right)  // 2
        if num < arr[mid]:
            right = mid - 1
        elif num > arr[mid]:
            left = mid + 1
        else:
            return mid
        
    return -1

a = [1]
index  = binary_search1(a,10)
print(index)