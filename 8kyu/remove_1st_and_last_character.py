#problem:Remove First and Last Character
#https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0/python

def remove_char(s):
    new_string = ''
    b = s[1::1]
    new_string += b
    c = new_string[0:-1:1]
    return c