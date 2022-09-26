nota1 = float(input('Nota 1: '))
por1 = float(input('Porcenaje 1: '))
nota2 = float(input('Nota 2: '))
por2 = float(input('Porcenaje 2: '))
nota3 = float(input('Nota 3: '))
por3 = float(input('Porcenaje 3: '))
promedio = nota1 * por1/100 + nota2 * por2/100 + nota3 * por3/100
if promedio >= 4.0:
    mensaje = "Aprobado"
else:
    mensaje = "Reprobado"
print ('Estado: ', mensaje, "Con nota: ", promedio)

