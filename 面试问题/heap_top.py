#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :heap_top.py
@说明        :
@时间        :2020/05/12 00:10:29
@作者        :gbw
@版本        :1.0
'''

def shift(heap, low ,high ):
    tmp = heap[low]
    i = low
    j = 2 * i + 1
    #子树
    while j <= high:
        # 右孩子存在并且小于左孩子
        if j + 1 <= high and heap[j + 1] < heap[j]:
            j += 1
        if tmp > heap[j]:
            heap[i] = heap[j]
            i = j
            j = 2 * i + 1
        else:
            break
    heap[i] = tmp

    return heap


def top_k(arr, k):
    heap = arr[:k]
    for i in range(k // 2 - 1, -1, -1):
        shift(heap, i, k - 1)

    for i in range(k, len(arr)):
        if arr[i] > heap[0]:
            heap[0] = arr[i]
            shift(heap, 0, k-1)
    
    return heap

li = [0, 8, 6, 2, 4, 9, 1, 4, 6]
print(top_k(li, 6))