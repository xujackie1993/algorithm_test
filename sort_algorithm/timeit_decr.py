#!/usr/bin/env python
# -*- coding: utf-8 -*-
from timeit import timeit
from functools import wraps

def time_it(func):

    @wraps(func)
    def wrappers(*args, **kwargs):
        result = func(*args, **kwargs)
        t = timeit('func()', 'from __main__ import func', number=1000)
        print(t)
        return result

    return wrappers

