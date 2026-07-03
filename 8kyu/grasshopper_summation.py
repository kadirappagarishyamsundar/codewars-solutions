#problem:Grasshopper - Summation
#https://www.codewars.com/kata/55d24f55d7dd296eb9000030

def summation(num):
    summ = 0
    for n in range(1,num+1):   # int is not iterable so use this range(1,num+1)
        summ = n*(n+1)//2
    return summ