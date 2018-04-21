'''
regex cheatsheet
. dowolny znak
[a-z] znak z zakresu
[^a-z] znak spoza zakresu 
^ poczatek napisu/linii
$ koniec napisu/linii
* dowolna ilosc powtorzen
? 0 lub jedno powtorzenie
+ jedno lub wiecej powtorzen
{n,m} od n do m powtorzen
() pod-wyrazenie (dla operatorow powtorzen/referencji wstecznych)

'''

import re
y = 'aa bb cc bb dd bb ee'

if re.match(".*bd", y):
    print(y, "zawiera b lub d")

#zastepowanie
print(re.sub('[bc]+', 'XX', y, 2))
print(re.sub('[bc]+', 'XX', y))
