#problem:Shortest Word
#https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9

def find_short(s):
    min_len = len(s)
    current_word_len = 0
    for char in s + " ":
        if char != " ":
            current_word_len += 1
        else:
            if current_word_len > 0:
                min_len = min(min_len,current_word_len)
            current_word_len = 0
    return min_len