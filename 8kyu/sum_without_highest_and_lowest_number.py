#problem:Sum without highest and lowest number
#https://www.codewars.com/kata/576b93db1129fcf2200001e6

def sum_array(arr):
    if not arr or len(arr) <= 2:  # guard clause for None or small arrays
        return 0
    highest = arr[0]  # Track highest,lowest, and summ
    lowest = arr[0]
    summ = 0
    for num in arr:  # Loop through the arr and check the highest and lowest num
        if num > highest:
            highest = num
        if num < lowest:
            lowest = num
        summ += num  # add it to the summ
    return summ - highest - lowest  # returnung the sum with subtracting highest and lowest
