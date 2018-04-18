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