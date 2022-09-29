suma = 0
i = 0
n = int(input('Ingrese la cantidad de estudiantes: '))
while i < n:
    nota = float(input('Nota : '))
    suma = suma + nota
    i = i + 1
promedio = suma / n
print('Promedio: ', promedio)
