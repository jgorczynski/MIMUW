def skrot(a):
    for x in a:
        print(x[0] + "-" + x[-1], '('+str(len(x))+')')

l = ['Interdyscyplinarne', 'Centrum', 'Modelowania']
skrot(l)