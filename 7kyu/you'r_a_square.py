#problem:You're a square!
#https://www.codewars.com/kata/54c27a33fb7da0db0100040e

def is_square(n):
    root = n**0.5
    if n < 0 or root * root != n:
        return False
    elif root * root == n:
        return True