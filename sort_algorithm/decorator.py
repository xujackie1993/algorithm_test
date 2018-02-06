#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import functools

def timeit(func):
    '''
    loggind for function execution duration
    '''
    @functools.wraps(func)
    def wrappers(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        print("Time cost {duration}".format(duration=time.time() - start_time))
        return result

    return wrappers

