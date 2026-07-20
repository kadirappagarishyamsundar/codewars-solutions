#problem:Replace With Alphabet Position
#https://www.codewars.com/kata/546f922b54af40e1e90001da

def alphabet_position(text):
    # make the text to lower cases
    str_ = text.lower()
    # take one empty list
    result = []
    #loop through the text, if it is char, ascii - 96
    for char in str_:
        if char.isalpha():
            position = str(ord(char) - 96)
            #append the position to result
            result.append(position)
    return " ".join(result)
