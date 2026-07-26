#problem:Build a pile of Cubes
#https://www.codewars.com/kata/5592e3bd57b64d00f3000047/python

import math
def find_nb(m):
    s = math.isqrt(m)
    if  s*s != m:
        return -1
    disc = 1 + 8 * s
    r = math.isqrt(disc)

    if r * r == disc and (r -1) %2 == 0:
        n = (r-1) // 2
        return n
    return -1
    