#problem:Count characters in your string
#https://www.codewars.com/kata/52efefcbcdf57161d4000091/python

from collections import Counter
def count(s):
    res = {}
    dict(Counter(s))
    for i in s:
        if i in res:
            res[i]+=1
        else:
            res[i] = 1
    return res