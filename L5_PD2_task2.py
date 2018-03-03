#zadanie 2

alfabet='AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻ'
def cezar(slowo,klucz):
  regula = str.maketrans(alfabet,alfabet[klucz:] + alfabet[:klucz])
  print (slowo.translate(regula))

def szyfruj_liste(lista):
  for x in lista:
    key = len(x)
    cezar(x, key)
    

###