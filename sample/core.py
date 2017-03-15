# -*- coding: utf-8 -*-

def add(a, b):
    """Add two numbers"""

    if((type(a) is bool) and (type(b) is bool)):
        return a or b
    if((type(a) is bool) and not(type(b) is bool)):
        return TypeError
    if(not(type(a) is bool) and (type(b) is bool)):
        return TypeError
    if ((type(b) is str) or (type(a) is str)):
        a = str(a)
        b = str(b)
    return a + b

def count(str):
    """Count words"""
    import collections
    from collections import Counter

    sentence = str.lower()
    list = sentence.split()
    count = collections.Counter(list)

    return count

if __name__ == "__main__":
    count("str")