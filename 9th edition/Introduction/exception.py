try:
    a = 5/0
except ZeroDivisionError:
    print('dzielenie przez zero')
except:
    print('inny blad')

#pass - ignore the exception
try: 
    slownik['a'] += 1
except:
    pass

#we can also generate exceptions from our code with 'raise' command. it has to be passed -> object that inherits after BaseException

raise BaseException("some fault")
