#problem:Opposites Attract
#https://www.codewars.com/kata/555086d53eac039a2a000083/solutions/python

def lovefunc( flower1, flower2 ):
    if flower1%2 == 0 and flower2%2 != 0 or flower1%2!=0 and flower2%2 == 0:
        return True
    else:
        return False