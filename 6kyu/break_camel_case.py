#problem:Break camelCase
#https://www.codewars.com/kata/5208f99aee097e6552000148
def solution(s):
    my_string = ""
    for i in s:
        if i.islower():
            my_string += i
        elif i.isupper():
            my_string += " " + i
    return my_string