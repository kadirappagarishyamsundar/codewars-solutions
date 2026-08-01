#problem:Maximum subarray sum
#https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c/python

def max_sequence(arr):
    max_so_far = 0
    max_ending_here = 0

    for num in arr:

        # update current max sum(either add num or start fresh)
        max_ending_here = max(0,max_ending_here + num)

        #update overall max
        max_so_far = max(max_so_far,max_ending_here)

    return max_so_far