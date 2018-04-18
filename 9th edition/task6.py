def zlicz(a):
    count_me = 0
    for i in range(len(a)):
        if a[i] in a: 
            count_me += 1
        print(str(a[i]) + " wystepuje " + str(count_me) + " razy")

zlicz(['a', 'b', 'a'])
