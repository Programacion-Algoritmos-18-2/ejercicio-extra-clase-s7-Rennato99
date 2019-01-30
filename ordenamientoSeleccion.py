class OrdenamientoSeleccion(object):
	# Constructor
	def __init__(self, datos):
		self.datos = datos

	# Metodo de Ordenamiento Seleccion
	def ordenar(self):
		self.iteraciones = 0

		# itera a traves de datos.length - 1 elementos
		i = 0
		while (i < len(self.datos)-1):

			masPequenio = i # primer indice del resto del arreglo

			# itera para buscar el indice del elemento mas pequeno
			indice = i + 1
			while (indice < len(self.datos)):
				if (self.datos[indice] < self.datos[masPequenio]) :
					masPequenio = indice
				indice += 1

			i += 1

			self.intercambiar(i, masPequenio) # intercambia el elemento mas pequeno en la posicion
			# imprimirPasada(i + 1, masPequenio) # imprime la pasada del algoritmo
			self.iteraciones += 1
			print(self.__str__())



	# Metodo ayudante para intercambiar los valores de dos elementos
	def intercambiar(self, primero, segundo):
		temporal = self.datos[primero]		 	# almacena primero en temporal
		self.datos[primero] = self.datos[segundo] 	# sustituye primero con segundo
		self.datos[segundo] = temporal 			# coloca temporal en segundo


	# Metodo que representa al objeto
	def __str__(self):
		temporal = "["
		for elemento in self.datos:
			temporal += " "+str(elemento)
		temporal += " ]\nNumero de iteraciones = "+str(self.iteraciones)
		return temporal
