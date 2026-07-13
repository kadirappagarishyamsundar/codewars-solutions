#problem:Duplicate Encoder
#https://www.codewars.com/kata/54b42f9314d9229fd6000d9c

def duplicate_encode(word):
    word = word.lower()
    result = ""
    for char in word:
        if word.count(char) == 1:
            result += '('
        else:
            result += ')'
    return result
