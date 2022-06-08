#----------------------------PROMEDIO 3--------------------------------#
# 19/07/2021
# Santiago, Chile
# Eddie Casañas
#----------------------------------------------------------------------#

def verificarNota(nota):
	if nota < 1 or nota > 7:
		print("\nPor favor, introduzca un numero en el rango especificado\n")
		return False
	else:
		return True
		
def notas(asignaturas):
	print("\nIntroducir notas en el rango del 1 al 7\n")
	notas_totales = []
	n = 0
	while n < int(asignaturas):
		print("\nPROMEDIO DE LA ASIGNATURA #" + (str(n + 1)))
		try:
			calificacion = float(input("Introduzca la primera nota: "))
			if verificarNota(calificacion) == False:
				continue
			calificacion_2 = float(input("Introduzca la segunda nota: "))
			if verificarNota(calificacion_2) == False:
				continue
			calificacion_3 = float(input("Introduzca la tercera nota: "))
			if verificarNota(calificacion_3) == False:
				continue
			promedio = (calificacion + calificacion_2 + calificacion_3)/3
			asignatura = n + 1
			print("\nPROMEDIO DE LA ASIGNATURA " + str(asignatura) + ":\n ")
			print(promedio)
			notas_totales.append(promedio)
			n += 1
			
		except:
			print("\nPor favor, introduzca un numero valido\n")
			
	return notas_totales
	
		
def promedio():
	while True:
		try:
			numero_asignaturas = int(input("\nIngrese el numero de asignaturas a calcular: "))
			notas_totales = notas(numero_asignaturas)
			print("\nCALCULO DEL PROMEDIO TOTAL: ")
			promedio_total = sum(notas_totales)/len(notas_totales)
			print(promedio_total)
			print("\nPROMEDIO REDONDEADO: ")
			print(round(promedio_total))
		except:
			print("Ingrese un numero valido\n")
			continue
		else:
			break
		
		
		
def salida():
	
	pregunta = input("¿Desea calcular otro promedio? (y/n) ")
	if pregunta.lower().strip() == "y":	
		promedio()
		
	elif pregunta.lower().strip() == "n":
		return 1
			
		
			


promedio()
while True:
	salir = salida()
	if salir == 1:
		break
