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

def count(text):
    """Count words"""
    import collections
    from collections import Counter

    if(type(text) is str):
        for i in range(len(text)):
            if not(((ord(text[i]) >= 48) and (ord(text[i]) <= 57)) or ((ord(text[i]) >= 65) and (ord(text[i]) <= 90)) or ((ord(text[i]) >= 97) and (ord(text[i]) <= 122))):
                text = text.replace(text[i], ' ')

    print(text)
    sentence = text.lower()
    list = sentence.split()
    count = collections.Counter(list)

    return count

if __name__ == "__main__":
    count("text")