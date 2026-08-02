#problem:Testing 1-2-3
#https://www.codewars.com/kata/54bf85e3d5b56c7a05000cf9

def number(lines):
    length = len(lines)
    res = []
    for idx,n in enumerate(lines):
        res.append (f"{idx+1}: {n}")
    return res