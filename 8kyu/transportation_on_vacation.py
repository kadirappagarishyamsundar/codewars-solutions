#problem:Transportation on vacation
#https://www.codewars.com/kata/568d0dd208ee69389d000016

def rental_car_cost(days):
    total_amount = 0
    if days >= 7:
        total_amount = days * 40
        return total_amount - 50
    elif days >= 3:
        total_amount = days * 40
        return total_amount - 20
    else:
        total_amount = days * 40
        return total_amount
