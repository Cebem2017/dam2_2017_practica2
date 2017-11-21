import datetime
ahora=datetime.datetime.now()
print("Hora actual: "+ahora.strftime("%H:%M"))
salida=datetime.datetime.now()
salida=salida.replace(hour=15, minute=00)
print("Hora de salida: "+salida.strftime("%H:%M"))
faltan=salida-ahora
print("Faltan para salir: "+str(faltan))