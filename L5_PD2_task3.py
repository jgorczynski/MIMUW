#zadanie 3
alfabet1 = 'AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻ'
alfabet2 = 'aąbcćdeęfghijklłmnńoóprsśtuwyzźż'

def cezar(slowo,klucz):
  alfabet = alfabet1 + alfabet2
  regula = str.maketrans(alfabet,alfabet[klucz:] + alfabet[:klucz])
  print (slowo.translate(regula), end='')  

def szyfruj_napis(napis, klucz):
  for x in napis:
    if x in alfabet1 or alfabet2:
      cezar(x, klucz)
    else:
      print(x, end='')
      

###