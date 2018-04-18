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


