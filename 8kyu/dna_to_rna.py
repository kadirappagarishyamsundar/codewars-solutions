#problem:DNA to RNA Conversion
#https://www.codewars.com/kata/5556282156230d0e5e000089

def dna_to_rna(dna):
    result = ''
    for char in dna:
        if char == 'T':
            result += 'U'
        else:
            result += char
    return result






