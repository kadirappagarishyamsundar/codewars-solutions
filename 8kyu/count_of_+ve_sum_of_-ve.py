#problem:Count of positives / sum of negatives.
#https://www.codewars.com/kata/576bb71bbbcf0951d5000044

def count_positives_sum_negatives(arr):
    count = 0
    sum = 0
    if not arr:
        return []
    for n in arr:
        if n>0:
            count += 1
        if n<0:
            sum +=n

    return[count, sum]