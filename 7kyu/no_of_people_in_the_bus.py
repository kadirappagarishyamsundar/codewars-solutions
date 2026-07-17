#problem:Number of People in the Bus
#https://www.codewars.com/kata/5648b12ce68d9daa6b000099

def number(bus_stops):
    result = []
    for sublist in bus_stops:
        for num in sublist:
            result.append(num)
    a = sum(result[0::2])
    b = sum(result[1::2])
    return a - b





