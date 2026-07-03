#problem:Square(n) Sum
#https://www.codewars.com/kata/515e271a311df0350d00000f

def square_sum(numbers):
    total = 0
    for num in numbers:
        total += num**2
    return total