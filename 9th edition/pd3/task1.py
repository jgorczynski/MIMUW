plik = open('tekst.txt', 'rt', encoding='utf8')
for s in plik:
  print(s[::5], end='')
plik.close()
