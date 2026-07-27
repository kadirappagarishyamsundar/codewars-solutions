#problem:Bouncing Balls
#https://www.codewars.com/kata/5544c7a5cb454edb3c000047

def bouncing_ball(h, bounce, window):
    if not(h>0 and bounce>0 and bounce<1 and window <h):
        return -1
    count = 1
    while h * bounce > window:
        count +=2
        h = h * bounce
    return count