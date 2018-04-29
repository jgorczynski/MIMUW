
def list_to_dict(l):
    d = {}
    s = "="
    for a in l:
        b = a.find(s)
        c = a.split('=', b)
        d[c[0]] = c[1]
    print(d)

l = ['aa=13', 'b=Ala=kot', 'f=xyz']

list_to_dict(l)
