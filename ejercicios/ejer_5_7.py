#Desarrollar un algoritmo que encuentre todos 
# los números primos menores o iguales a un cierto 
# numero ingresado por teclado.

def lista_de_primos(n):
    primos = [1, 2, 3]
    i = 4
    while i <= n:
        di = 2
        ok = False
        while di < i:
            if (i % di) == 0:
                ok = True
            di = di + 1
        if ok == False:
            primos.append(i)
        i = i + 1
    return primos  

if __name__ == '__main__':
    n = int(input('Numero n: '))
    primos = lista_de_primos(n)
    print(primos)
