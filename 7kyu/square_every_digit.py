#problem:Square Every Digit
#https://www.codewars.com/kata/546e2562b03326a88e000020/solutions/python

def square_digits(num):
    result = ""
    a = str(num)
    for n in a:
        squared = int(n)*int(n)
        result += str(squared)
    return int(result)