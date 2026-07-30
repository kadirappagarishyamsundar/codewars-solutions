#problem:Consecutive strings
#https://www.codewars.com/kata/56a5d994ac971f1ac500003e

def longest_consec(strarr, k):
    s = len(strarr)
    if s == 0 or k<=0 or k > s :
        return ""
    longest = ""
    for i in range(s - k + 1):
        current_str = "".join(strarr[i : i + k])
        if len(current_str) > len(longest):
            longest = current_str
    return longest
