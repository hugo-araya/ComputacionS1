def funcion1(x):
    resultado = 2*x+1
    return resultado

def funcion2(x):
    resultado = x * x
    return resultado

if __name__ == '__main__':
    print(funcion2(funcion1(5)))
    print(__name__)

