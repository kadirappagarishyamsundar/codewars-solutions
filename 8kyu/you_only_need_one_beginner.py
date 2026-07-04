#problem:You only need one - Beginner
#https://www.codewars.com/kata/57cc975ed542d3148f00015b/python

def check(seq, elem):
    result = []          # we first create an empty list
    for i in seq:         # loop through the seq, add it to the result
        result.append(i)
    if elem in result:     # find is elem present in the seq, true if there, false if not
        return True
    else:
        return False