#problem:Complementary DNA
#https://www.codewars.com/kata/554e4a2f232cdd87d9000038

def DNA_strand(dna):
    dna_list = ''
    for char in dna:
        if char == 'A':
            dna_list += 'T'
        if char == 'T':
            dna_list += 'A'
        if char == 'G':
            dna_list += 'C'
        if char == 'C':
            dna_list += 'G'
    return dna_list