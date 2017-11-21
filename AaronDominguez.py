import random

def crear_numero():
    return random.randrange(10)


puntuacion = 0
numero_operaciones = 0

print("Introduce cuantas operaciones quieres realizar.")
numero_operaciones = input()


i = 0
while i<int(numero_operaciones):
    i +=1
    primer_digito = crear_numero()
    segundo_digito = crear_numero()
    
    print(primer_digito," + ",segundo_digito)
    resultado = input()
    resultado =  int(resultado)
    resultado_correcto = int(primer_digito) + int(segundo_digito)
    if int(resultado_correcto) == resultado:
        puntuacion+=1
        print("Correcto!")

print("Tu puntuacion es de ", puntuacion)