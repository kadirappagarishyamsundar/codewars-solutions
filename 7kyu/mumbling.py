#problem:Mumbling
#https://www.codewars.com/kata/5667e8f4e3f572a8f2000039

def accum(st):
    length = len(st)
    #storing result
    res = []
    #use enumerate method to take both index and char
    for idx, s in enumerate(st):
        parts = s.upper() + (idx * s.lower())
        res.append(parts)
    return '-'.join(res)
