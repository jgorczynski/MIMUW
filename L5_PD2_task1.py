#zadanie 1

alfabet="aąbcćdeęfghijklłmnńoóprsśtuwyzźż"
def cezar(slowo,klucz):
  regula = str.maketrans(alfabet,alfabet[klucz:] + alfabet[:klucz])
  print (slowo.translate(regula))

string = 'zweśńhćóubęśńk'
for key in range(1,32):
  print(key, end=' ')
  cezar(string, key)
