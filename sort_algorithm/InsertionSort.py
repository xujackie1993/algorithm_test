#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
插入排序
'''
def insert_sort(arry):
    n = len(arry)
    for i in range(1,n):
        if arry[i] < arry[i-1]:
            temp = arry[i]
            index = i   #带插入的下标
            for j in range(i-1,-1,-1):
                if arry[j] > temp:
                    arry[j+1] = arry[j]
                    index = j
                else:
                    break

            arry[index] = temp

    return arry

print(insert_sort([4,1,2]))