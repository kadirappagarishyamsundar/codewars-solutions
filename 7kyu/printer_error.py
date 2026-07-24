#problem:Printer Errors
#https://www.codewars.com/kata/56541980fa08ab47a0000040

def printer_error(s):
    n = len(s)
    count = 0
    for char in s:
        if char not in "abcdefghijklm":
            count += 1
    return f"{count}/{n}"