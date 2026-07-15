#problem:Sum of two lowest positive integers
#https://www.codewars.com/kata/558fc85d8fd1938afb000014

def sum_two_smallest_numbers(numbers):
    smallest_number = float('inf')
    second_smallest_number = float('inf')
    for n in numbers:
        if n < smallest_number:
            second_smallest_number = smallest_number
            smallest_number = n
        elif n < second_smallest_number:
            second_smallest_number = n
    return smallest_number + second_smallest_number



