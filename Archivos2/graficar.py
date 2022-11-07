import matplotlib.pyplot as plt

ar = open('TotalesNacionalesActualizado.csv')
linea1 = ar.readline()
linea2 = ar.readline()
linea2 = linea2.rstrip('\n')
lista1 = linea2.split(',')
ar.close()
lista2 = []
for elem in lista1:
    lista2.append(float(elem))
print(lista2)
plt.plot(lista2)
plt.title('Contagios')
plt.show()
