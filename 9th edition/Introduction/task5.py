#split, find, replace

def parse(s):
    s1 = s.replace('XY', ' ').split(':')
    print(s1)

l = parse('Ala:maXYkota:i inne:zwierzeta')
