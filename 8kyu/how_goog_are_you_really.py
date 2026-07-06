#problem:How good are you really?
#https://www.codewars.com/kata/5601409514fc93442500010b

def better_than_average(class_points, your_points):
    points = 0
    for n in class_points:
        points = n + points
    class_avg = points/len(class_points)
    if class_avg < your_points:
        return True
    else:
        return False