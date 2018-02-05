#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''选择排序
'''
def select_sort(arry):
    n = len(arry)
    for i in range(0,n):
        min = i         #最小元素下标标记
        for j in range(i+1,n):
            if arry[j] < arry[min]:
                min = j       #找到最小值的下标

        arry[min], arry[i] = arry[i], arry[min]   #交换两者

    return arry

print(select_sort([7,5,8,4,6]))
