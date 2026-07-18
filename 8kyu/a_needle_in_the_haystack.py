#problem:A Needle in the Haystack
#https://www.codewars.com/kata/56676e8fabd2d1ff3000000c/python

def find_needle(haystack):
    for index, char in enumerate(haystack):
        if char == "needle":
            return f"found the needle at position {index}"



