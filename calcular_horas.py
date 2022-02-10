#este programa calcula la hora que será con respecto a la duración en minutos del evento

hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

suma_minutos = mins + dura
nuevos_minutos = suma_minutos % 60 #duración de 1 hora
horas_agregadas = suma_minutos // 60 
suma_horas = horas_agregadas + hour
nueva_hora = suma_horas % 24

print(nueva_hora, nuevos_minutos, sep=":")