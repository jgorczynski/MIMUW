#find sum of 1**2 + 2**2 + ... + 99**2 + 100**2

suma = 0
for x in range(1, 101):
    suma += x**2
print(suma)