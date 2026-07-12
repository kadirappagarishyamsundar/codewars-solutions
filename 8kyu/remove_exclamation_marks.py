#problem:Remove exclamation marks
#https://www.codewars.com/kata/57a0885cbb9944e24c00008e

def remove_exclamation_marks(s):
    result = ""
    for char in s:
        if char != '!':
            result += char
    return result