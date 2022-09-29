suma = 0
i = 0
minima = 8
maxima = -1
n = int(input('Ingrese la cantidad de estudiantes: '))
while i < n:
    nota = float(input('Nota : '))
    suma = suma + nota
    if nota <= minima:
        minima = nota
    if nota >= maxima:
        maxima = nota
    i = i + 1
promedio = suma / n
print('Promedio: ', promedio)
print('La mas baja: ', minima)
print('La mas alta: ', maxima)