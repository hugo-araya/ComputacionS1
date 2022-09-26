nota1 = float(input('Nota 1: '))
por1 = float(input('Porcentaje nota 1: '))
nota2 = float(input('Nota 2: '))
por2 = float(input('Porcentaje nota 2: '))
#nota3 = float(input('Nota 3: '))
por3 = float(input('Porcentaje nota 3: '))
acumulado = nota1*por1/100 + nota2*por2/100
falta = 4 - acumulado
print('Necesito un : ', falta/(por3/100))
