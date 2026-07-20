#problem:Playing with digit
#https://www.codewars.com/kata/5552101f47fc5178b1000050

def dig_pow(n, p):
    str_ = str(n)
    result = 0
    for i in str_:
        digit = int(i)
        d = (digit**p)
        result += d
        p += 1
    if result % n == 0:
        k = result//n
        return k
    else:
        return -1