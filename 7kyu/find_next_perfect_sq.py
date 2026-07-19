#problem:Find the next perfect square!
#https://www.codewars.com/kata/56269eb78ad2e4ced1000013

def find_next_square(sq):
    root = int(sq**0.5)
    if sq < 0 or root * root !=sq :
        return -1
    else:
        return (root+1)**2