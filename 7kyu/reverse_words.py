#problem:Reverse words
#https://www.codewars.com/kata/5259b20d6021e9e14c0010d4
def reverse_words(text):
    result = ""
    words = ""

    for i in text:
        if i == " ":
            # if we hit with a space add words with reverse in to the result
            result += words[::-1] + " "
            words = ""
        else:
            # Accumulate characters in words
            words += i

    # don't forget the very last word doesn't might not end with space
    result += words[::-1]
    return result    