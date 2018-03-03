lista = ['Ala', 'ma', 'kota']
output = ''

for slowo in lista:
    for i in range(len(slowo), 0, -1):
        output += slowo[i-1]
    print(output)
    output = ''

print()
#NOTE:  Znalazłem też szybsze rozwiązanie jednopętlowe (przy małej pomocy dokumentacji):

#zadanie 3.1 
for x in lista:
    print(x[::-1])