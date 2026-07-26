#problem:Count the smiley faces!
#https://www.codewars.com/kata/583203e6eb35d7980400002a/python

import re
def count_smileys(arr):
    pattern = r"^[:;][-~]?[)D]$"
    return sum(1 for face in arr if re.match(pattern, face))