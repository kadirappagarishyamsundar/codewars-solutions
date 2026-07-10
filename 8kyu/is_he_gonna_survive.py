#problem:Is he gonna survive?
#https://www.codewars.com/kata/59ca8246d751df55cc00014c

def hero(bullets, dragons):
    survive = bullets//dragons
    if survive == 2:
        return True
    return False