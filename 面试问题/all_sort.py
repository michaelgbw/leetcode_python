#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :all_sort.py
@说明        :
@时间        :2020/05/11 23:53:42
@作者        :gbw
@版本        :1.0
'''
import random

#冒泡
def bubble_sort(arr):
    length = len(arr)
    for i in range(length - 1):
        for j in range(length - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

#选择排序
def selection_sort(arr):
    length = len(arr)
    for i in range(length - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[i]:
                arr[j], arr[i] = arr[i], arr[j]


#插入排序
def insert_sort(arr):
    for i in range(1, len(arr)):
        # 从第二个元素开始，每次取出一个元素，插入前面的序列使其有序
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]


def quick_sort(arr):
    pirot = random.sample(arr,1)[0]

    low_list = [ ]
    high_list = [ ]
    eq_list = [ ]
    for one in arr:
        if one < pirot: low_list.append(one)
        if one > pirot: high_list.append(one)
        if one == pirot: eq_list.append(one)

    return quick_sort(low_list) + eq_list + quick_sort(high_list)