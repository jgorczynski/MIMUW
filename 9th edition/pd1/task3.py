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

l = ['Ala', 'ma', 'kota', 'i PSA']

two(l)

#or with str.replace()

def two_replace(a):
    b = 'aąbcćdeęfghijklłmnńoóprsśtuwyzźż'
    for x in a:
        x1=x #that's the one that was missing
        for y in x:
            if y in b:
                x1 = x1.replace(y, 2*y)
        print(x1)

two_replace(l)
