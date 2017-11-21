# -*- coding: utf-8 -*-
def areaCirculo():
    radio = float(input('Radio: '))
    return 3.14159 * 2 * radio


def areaRectangulo():
    base = float(input('Base: '))
    altura = float(input('Altura: '))
    return base * altura


def areaTriangulo():
    base = float(input('Base: '))
    altura = float(input('Altura: '))
    return (base * altura) / 2


print('CALCULAR ÁREA \n 1-Círculo \n 2-Rectángulo \n 3-Triángulo')
figura = input("Seleccione una opción: ")

if (figura == '1'):
    print('ÁREA: ', areaCirculo())
elif (figura == '2'):
    print('ÁREA: ', areaRectangulo())
elif (figura == '3'):
    print('ÁREA: ', areaTriangulo())
else:
    print('Error. La operación solicitada no existe')
