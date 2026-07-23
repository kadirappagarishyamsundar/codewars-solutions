#problem:Tribonacci Sequence
#https://www.codewars.com/kata/556deca17c58da83c00002db

def tribonacci(signature, n):
    if n == 0:
        return []
    elif n <3:
        return signature[:n]
    result = signature[:]
    while len(result)<n:
        next_val = sum(result[-3:])
        result.append(next_val)
        len(result) == n
    return result