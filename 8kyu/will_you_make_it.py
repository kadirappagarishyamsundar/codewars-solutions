#problem:Will you make it?
#https://www.codewars.com/kata/5861d28f124b35723e00005e

def zero_fuel(distance_to_pump, mpg, fuel_left):
    a = distance_to_pump
    b = mpg
    c = fuel_left
    if b * c >= a:
        return True
    else:
        return False