ar = open('datos.dat')
x1 = []
y1 = []
paso = []
for linea in ar:
    linea = linea.rstrip('\n')
    print(linea)
    lista = linea.split(' ')
    print(lista)
    linea1 = lista[0]
    print(linea1)
    lista1 = linea1.split('-')
    print(lista1)
