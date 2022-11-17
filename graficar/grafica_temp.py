import matplotlib.pyplot as plt
def lee_datos(nombre):
    ar = open(nombre)
    x1 = []
    y1 = []
    paso = []
    for linea in ar:
        linea = linea.rstrip('\n')
        separa = linea.split(' ')
        elem0 = separa[0]
        elem1 = separa[1]
        fecha = elem0.split('-')
        if elem1 < '10':
            temp = '0'+elem1
        else:
            temp = elem1
        datoreal = fecha[2]+fecha[1]+fecha[0]+ temp
        paso.append(datoreal)
        
    paso.sort()
    for elem in paso:
        x1.append(elem[2:6])
        y1.append(int(elem[6:]))
    return x1, y1

if __name__ == '__main__':
    x, y = lee_datos('datos.dat')
    fig, ax = plt.subplots()
    ax.bar(x, y) 
    plt.show()