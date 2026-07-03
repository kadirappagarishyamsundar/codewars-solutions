#problem:Sum of positive
#https://www.codewars.com/kata/5715eaedb436cf5606000381

def positive_sum(arr):
    sum = 0  # initialize a number to keep track of the sum
    for num in arr:  # Loop through the array
        if num > 0:  # if num is greater than 0 means positive
            sum = sum + num  # add it to the sum
    return sum  # give the result of the sum
