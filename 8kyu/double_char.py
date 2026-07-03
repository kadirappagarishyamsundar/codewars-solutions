#problem:Double Char
#https://www.codewars.com/kata/56b1f01c247c01db92000076


def double_char(s):
    result = ""         # take an empty string
    for char in s:      # loop through char by char in s
        result = result + (char * 2) # char + char / char *2 to double it.
    return result