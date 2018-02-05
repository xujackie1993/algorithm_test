#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
实现lru算法（最近最少使用算法）
'''
import collections
from functools import lru_cache

class LRUCache(object):
    '''
    function: 利用collections.OrderedDict 数据类型实现 最近最少使用算法
            OrderedDict 有一个特殊的方法 popitem(last=False) 即实现队列，弹出最先插入的元素
            当last = True 则实现堆栈方法，弹出最近插入的那个元素
            实现两个方法：即get(key) 取出键中对应的值，若没有返回None
                        set(key, value)根据LRU特性添加元素
    '''
    def __init__(self,size=5):
        self.size = size
        self.cache = collections.OrderedDict()

    def get(self, key):
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        else:
            return None

    def set(self, key, value):
        if key in self.cache:
            self.cache.pop(key)
            self.cache[key] = value
        elif self.size == len(self.cache):
            self.cache.popitem(last=False)
            self.cache[key] = value
        else:
            self.cache[key] = value

'''使用普通的dict和list实现'''
class Lrucache(object):

    def __init__(self, size=5):
        self.size = size
        self.cache = dict()
        self.keys = list()

    def get(self, key):
        if key in self.cache:
            self.keys.remove(key)
            self.keys.insert(0, key)
            return self.cache[key]
        else:
            return None
    def set(self, key, value):

        if key in self.cache:
            self.cache.pop(key)
            self.cache[key] = value
            self.keys.remove(key)
            self.keys.insert(0, key)

        elif self.size == len(self.keys):
            old_key = self.keys.pop()
            self.cache.pop(old_key)
            self.keys.insert(0, key)
            self.cache[key] = value

        else:
            self.cache[key] = value
            self.keys.insert(0, key)


if __name__=="__main__":
    lrucache = LRUCache(3)
    lrucache.set("a", 1)
    lrucache.set("b", 2)
    print(repr(lrucache.get("a")))
    lrucache.set("c", 3)
    lrucache.set("d", 4)
    print(lrucache.cache)
