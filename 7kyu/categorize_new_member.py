#problem:Categorize New Member
#https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa

def open_or_senior(data):
    result = []
    for member in data:
        age =  member[0]
        handicap =  member[1]
        if age>=55 and handicap>7:
            result.append("Senior")
        else:
            result.append("Open")
    return result