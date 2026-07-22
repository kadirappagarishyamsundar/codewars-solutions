#problem:Are You Playing Banjo?
#https://www.codewars.com/kata/53af2b8861023f1d88000832

def are_you_playing_banjo(name):
    if name[0] == "r" or name[0] == "R" :
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"