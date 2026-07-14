#problem:Highest and Lowest
#https://www.codewars.com/kata/554b4ac871d6813a03000035

def high_and_low(numbers):
    nums = [int(x) for x in numbers.split()]
    highest = nums[0]
    lowest = nums[0]
    for n in nums:
        if n>highest:
            highest = n
        elif n<lowest:
            lowest = n

    return f"{highest} {lowest}"

