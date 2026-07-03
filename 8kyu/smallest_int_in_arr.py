#problem:Find the smallest integer in the array
#https://www.codewars.com/kata/55a2d7ebe362935a210000b2

def find_smallest_int(arr):
    smallest = arr[0] # assume first number as the smallest number
    for num in arr:   # we want to go through the arr using for loop.
        if num < smallest: # number is less thean assumed one(smallest).
            smallest = num # replace the smallest with new number.
    return smallest # return back the smallest number in array