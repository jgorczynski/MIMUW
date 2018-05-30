import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt 

x = []
y = []
plik = open('dane.txt', 'rt', encoding = 'utf8')
linia = plik.readline()
x = linia.split()

linia1 = plik.readline()
y = linia1.split()

x1 = [float(a) for a in x]
y1 = [float(b) for b in y]

plt.plot(x1, y1, '.g')
plt.savefig('plot.png')

plik.close()