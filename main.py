import random


tabla = []
numeros = []
pmi = 0.25
pmg = 0.40


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def seleccion_paquete():
    numeros.clear()
    for n in range(int(paquetes)):
        numero = random.randint(1, len(tabla))
        numeros.append(numero)

    for l in numeros:
        print(l)


def numero_por_paquete():
    # lista = [1, 2, 3, 1, 2]
    res = dict(zip(numeros, map(lambda x: numeros.count(x), numeros)))
    print(res)
    for n in range(len(res)):
        tabla[n] = str(res.get(n+1)) + "," + tabla[n]
        # print('----------------')
        # print(res.get(n+1))

    # print(res)


if __name__ == '__main__':
    a = input("Ingrese el valor de A: ")
    b = input("Ingrese el valor de B: ")
    c = input("Ingrese el valor de C: ")
    contenedor = input("Ingrese el espacio del Contenedor: ")
    paquetes = input("Ingrese el numero de paquetes: ")

    tabla.append('A,' + a)
    tabla.append('B,' + b)
    tabla.append('C,' + c)

    for n in tabla:
        print(n)

    seleccion_paquete()

    numero_por_paquete()

    for l in tabla:
        print(l)