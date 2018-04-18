l = ['i', 'C', 0, 'M']
l[0] = 'I'
del l[2]
print(l)

for i in range(len(l)):
    print(l[i])
    l[i] = 'q'
print(l)

#editable string
s = 'abcdefgh'
l = list(s)
l[2] = 'X'
del(l[5])
s = "".join(l)
print(s)

#defining var type
a,b,c = 1, 3.14, 'Python'
print(a, type(a))
print(b, type(b))
print(c, type(c))
c = (a == 1)
print(c, type(c))

#objectivity
l = ['i', 'm']
l.insert(1, 'c')
print(l)
l.reverse()
print(l)
l.sort()
print(l)

#6.4 dictionaries - key-value pairs

slownik = {"bd" : "xx", 5 : True, "a" : 11}
for klucz in slownik: 
    print(klucz, "=>", slownik[klucz])

if "bd" in slownik:
    print("jest element o kluczu 'bd'")
    del slownik['bd']
slownik[15] = True
slownik['a'] = 'yy'
#for k, v in m.items():
    #print (k, "=>", v)




