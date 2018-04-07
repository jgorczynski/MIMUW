"""def dodaj():
    global b
    a,b = 5, 13
    print(a,b,c)
a,b,c = 1,3,7
dodaj()
print(a,b,c)"""

"""s = 'abcdefgh'
s = s[:2] + 'X' + s[3:5] + s[6:]
print(s)"""

#task 4

def wyiksuj(s):
    alfabet = "AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻ"
    alfabet1 = 'aąbcćdeęfghijklłmnńoóprsśtuwyzźż'
    #s, ns = 'Python 3.6.1 (default, Dec 2015, 13:05:11)', ''
    ns = ''
    for z in s:
        if z in alfabet:
            ns = ns + 'X'
        elif z in alfabet1:
            ns = ns + 'x'
        else:
            ns = ns + z
    print(ns)

wyiksuj('ALA ma KOTA')




