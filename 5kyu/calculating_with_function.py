#problem:Calculating with Functions
#https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39

def number_builder(number, func = None):
    return number if func is None else func(number)
def zero(func = None):
    return number_builder(0, func)
def one(func = None):
    return number_builder(1, func)
def two(func = None):
    return number_builder(2, func)
def three(func = None):
    return number_builder(3, func)
def four(func = None):
    return number_builder(4, func)
def five(func = None):
    return number_builder(5, func)
def six(func = None):
    return number_builder(6, func)
def seven(func = None):
    return number_builder(7, func)
def eight(func = None):
    return number_builder(8, func)
def nine(func = None):
    return number_builder(9, func)

def plus(y):    return lambda x: x + y
def minus(y):   return lambda x: x - y
def times(y):   return lambda x: x * y
def divided_by(y):   return lambda x: x // y