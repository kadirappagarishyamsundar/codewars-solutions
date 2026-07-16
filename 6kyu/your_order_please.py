#problem:Your order, please
#https://www.codewars.com/kata/55c45be3b2079eccff00010f/python

def order(sentence):
    if not sentence:
        return ""
    def get_digit(word):
        for char in word:
            if char.isdigit():
                return int(char)

    words = sentence.split()
    sorted_words = sorted(words, key = get_digit)

    return " ".join(sorted_words)
    



