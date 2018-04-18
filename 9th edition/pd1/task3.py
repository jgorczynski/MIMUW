def dwie_male(a):
    b = 'aąbcćdeęfghijklłmnńoóprsśtuwyzźż'
    for x in a:
        for y in x:
            if y in b:
                x1 = x.replace(y, 2*y)
        print(x1)


l = ['Ala', 'ma', 'kota', 'i PSA']

dwie_male(l)

def two(a):
    alfabet = 'aąbcćdeęfghijklłmnńoóprsśtuwyzźż'
    for x in a:
        na = ''
        for y in x:
            if y in alfabet:
                na = na + 2*y
            else:
                na = na + y
        print(na)

two(l)