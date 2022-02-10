def promedio(lista_datos):
    sumatoria = 0	
    total_datos = 0	
    for dato in lista_datos:
        sumatoria += dato
        total_datos += 1
    return sumatoria / total_datos	

def varianza_poblacion(lista_datos, promedio):		
	sumatoria = 0	
	total_datos = 0	
	for dato in lista_datos:	
		sumatoria += (dato - promedio)**2
		total_datos += 1
	return sumatoria / total_datos	
    
def varianza_muestra(lista_datos, promedio):		
	sumatoria = 0	
	total_datos = 0	
	for dato in lista_datos:	
		sumatoria += (dato - promedio)**2
		total_datos += 1
	return sumatoria / (total_datos	-1)

def desviacion_estandar(varianza):
	return varianza**.5

def frecuencia(lista_datos):
	frecuencia_dato = {}
	for dato in lista_datos:
		frecuencia_dato[dato] = lista_datos.count(dato)
	return frecuencia_dato

def dato_frec_a_lista(diccionario):
	lista = []
	for dato, instancias in diccionario.items():
		for i in range(instancias):
			lista.append(dato)
	return lista

def coeficiente_variacion(desviacion_estandar, promedio):
	return (desviacion_estandar / (abs(promedio) if promedio != 0 else 1)) * 100

entrada_datos = {13:3, 14:15, 15:23, 16:10, 17:5, 18:4}

lista_datos = dato_frec_a_lista(entrada_datos)
# lista_datos = [1,2,1,1,2,3]
promedio_datos = promedio(lista_datos)
varianza_poblacion_datos = varianza_poblacion(lista_datos, promedio_datos)
varianza_muestra_datos = varianza_muestra(lista_datos, promedio_datos)
desviacion_estandar_poblacion = desviacion_estandar(varianza_poblacion_datos)
desviacion_estandar_muestra = desviacion_estandar(varianza_muestra_datos)
frecuencia_datos = frecuencia(lista_datos)
coeficiente_variacion_poblacion = coeficiente_variacion(desviacion_estandar_poblacion, promedio_datos)
coeficiente_variacion_muestra = coeficiente_variacion(desviacion_estandar_muestra, promedio_datos)



print("datos:", lista_datos)
print('promedio:',promedio_datos)
print('varianza_poblacion:', varianza_poblacion_datos)
print("desviación estándar población:", desviacion_estandar_poblacion)
print("coeficiente variacion población:", coeficiente_variacion_poblacion)
print('varianza_muestra:', varianza_muestra_datos)
print("desviación estándar muestra:", desviacion_estandar_muestra)
print("coeficiente variacion muestra:", coeficiente_variacion_muestra)


