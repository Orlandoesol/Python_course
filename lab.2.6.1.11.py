hora = int(input("Hora de inicio (horas): "))
min = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))


# coloca tu código aqui
obtenerHora = (min + dura) // 60
obtenerMinuto = (min + dura) % 60
calcularHora = ((hora + obtenerHora) % 24)
print(calcularHora,":",obtenerMinuto,sep="")
print("***********************")
min = min + dura # encuentra el número total de minutos
hora = hora + min // 60 # encuentra el número de horas ocultas en los minutos y actualiza las horas
min = min % 60 # corrige los minutos para que estén en un rango de (0..59)
hora = hora % 24 # corrige las horas para que estén en un rango de (0..23) 
print(hora, ":", min, sep='')