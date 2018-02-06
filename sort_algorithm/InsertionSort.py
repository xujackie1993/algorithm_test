#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''插入排序
从第一个元素开始，该元素可以认为已经被排序
取出下一个元素，在已经排序的元素序列中从后向前扫描
如果被扫描的元素（已排序）大于新元素，将该元素后移一位
重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
将新元素插入到该位置后
重复步骤2~5'''

def insert_sort(arry):
    n = len(arry)
    for i in range(1,n):
        if arry[i] < arry[i-1]:
            temp = arry[i]
            index = i   #待插入的下标
            for j in range(i-1,-1,-1): #从i-1循环到0(包括0)
                if arry[j] > temp:
                    arry[j+1] = arry[j]
                    index = j     #记录待插入下标
                else:
                    break

            arry[index] = temp

    return arry

print(insert_sort([4,1,2]))

# def insert(arry):
#     n = len(arry)
#     for i in range(1,n):
#         if arry[i] < arry[i-1]:
#             temp = arry[i]
#             index = i
#             for j in range(i-1,-1,-1):
#                 if arry[j] > temp:
#                     arry[j+1] = arry[j]
#                     index = j
#
