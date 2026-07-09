#problem:String ends with?
#https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d

def solution(text, ending):
    # If ending is empty, it's always True
    if not ending:
        return True

    # Grab a slice from the end of text equal to the length of ending
    return text[-len(ending):] == ending