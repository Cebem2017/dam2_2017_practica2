#Programa que pide por teclado la nota numérica de un alumno y nos responde si está aprobado,
# suspendido, si tiene un bien o si tiene un     
nota = input("cual es tu nota del exámen")
nota = float(nota)

if nota >= 0 and nota < 5:
    print ('suspenso')
elif nota >= 5 and nota < 6:
    print ( 'suficiente' )
elif nota >= 6 and nota < 7:
    print ( 'bien' )
elif nota >= 7 and nota < 9:
    print ( 'notable' )
else :
    print ('excelente')