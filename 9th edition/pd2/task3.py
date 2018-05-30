
def list_to_dict(l):
    d = {}
    s = "="
    for a in l:
        b = a.find(s) # is that even necessary here?
        c = a.split('=', 1)
        d[c[0]] = c[1]
    print(d)

l = ['aa=13=4=aaa', 'ba=Ala=kot=psot', 'f=xyz=dd=0xffff']
m = ['aa=13', 'b=Ala=kot', 'f=xyz']
n = ['baa=Ala=kot']
list_to_dict(l)
list_to_dict(m)
list_to_dict(n)
