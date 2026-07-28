#problem:Is this a triangle?
#https://www.codewars.com/kata/56606694ec01347ce800001b

def is_triangle(a, b, c):
    a, b, c = sorted([a, b, c])
    return a>0 and a + b > c
