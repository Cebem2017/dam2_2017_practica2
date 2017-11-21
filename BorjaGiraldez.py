num1 = int(input('Primer numero: '))
num2 = int(input('Segundo numero: '))
contador = 0
aux = 0
aux1 = 0

if num1 > num2:
    aux = num2
    aux1 = num1
else:
    aux = num1
    aux1 = num2

while aux < aux1:
    contador += 1
    aux += 1

print('Entre {} y {} hay {} numeros'.format(num1, num2, contador))
