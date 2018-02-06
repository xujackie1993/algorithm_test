#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
from sort_algorithm.decorator import timeit

'''
快速排序
从数列中挑出一个元素作为基准数。
分区过程，将比基准数大的放到右边，小于或等于它的数都放到左边。
再对左右区间递归执行第二步，直至各区间只有一个数
'''
def quick_sort(ary):
    return qsort(ary,0,len(ary)-1)

def qsort(ary,left,right):
    #快排函数，ary为待排序数组，left为待排序的左边界，right为右边界
    if left >= right:
        return ary
    key = ary[left]     #取最左边的为基准数
    lp = left           #左指针
    rp = right          #右指针
    while lp < rp :
        while ary[rp] >= key and lp < rp :
            rp -= 1
        while ary[lp] <= key and lp < rp :
            lp += 1
        ary[lp],ary[rp] = ary[rp],ary[lp]
    ary[left],ary[lp] = ary[lp],ary[left]
    qsort(ary,left,lp-1)
    qsort(ary,rp+1,right)
    return ary

def func(arry):
    if not arry or len(arry) == 1:
        return arry
    base = arry[0]
    left_l, right_l = [], []
    for i in arry[1:]:
        if i >= base:
            right_l.append(i)
        else:
            left_l.append(i)
    left_l = func(left_l)
    right_l = func(right_l)
    return left_l + [base] + right_l

# print(func(l1))
#print(quick_sort([4,3,1,5,2]))

# arry = [1, 3, 19, 4, 8, 34, 89, 45, 20, 30, 79]
# print(func(arry))