#problem:Write Number in Expanded Form
#https://www.codewars.com/kata/5842df8ccbd22792a4000245

def expanded_form(num):
    digit = str(num)
    length = len(digit)
    parts = []
    for idx, i in enumerate(digit):
        if i != '0':
            zeros = length - 1 - idx
            parts.append(i + '0' * zeros)
    return ' + '.join(parts)