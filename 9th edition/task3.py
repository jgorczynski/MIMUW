#write a function sign(num) that gives an information about number sign and returns an absolute value

def sign(num):
    if num < 0:
        print('negative')
        return abs(num)
    elif num > 0:
        print('positive')
        return num
    else:
        print('zero')
        return num

a = sign(7)
b = sign(-13)
c = sign(0)

print(a,b,c)