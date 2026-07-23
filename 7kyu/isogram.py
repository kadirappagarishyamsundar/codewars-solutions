#problem:Isograms
#https://www.codewars.com/kata/54ba84be607a92aa900000f1

def is_isogram(string):
    s = string.lower()
    set1 = set(s)
    if len(set1) == len(s):
        return True
    else:
        return False