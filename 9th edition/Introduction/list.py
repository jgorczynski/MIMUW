l = ['i', 'C', 0, 'M']
l[0] = 'I'
del l[2]
print(l)

for i in range(len(l)):
    print(l[i])
    l[i] = 'q'
print(l)

