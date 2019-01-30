class OrdenamientoInsercion(object):

	# Constructor
	def __init__(self, datos):
		self.datos = datos


	# Metodo de Ordenamiento Insercion
	def ordenar(self):
		self.iteraciones = 0
		# itera a traves de datos.length - 1 elementos
		siguiente = 1
		while siguiente < len(self.datos):

			# almacena el valor en el elemento actual
			insercion = self.datos[siguiente]

			# inicializa ubicacion para colocar el elemento
			moverElemento = siguiente

			# busca un lugar para colocar el elemento actual
			while ( (moverElemento > 0) and (self.datos[moverElemento - 1] > insercion) ):

				# desplaza el elemento una posicion a la derecha
				self.datos[moverElemento] = self.datos[moverElemento - 1]
				moverElemento -= 1


			self.datos[moverElemento] = insercion # coloca el elemento insertado
			# imprimirPasada( siguiente, moverElemento ) # imprime la pasada del algoritmo
			self.iteraciones += 1
			print(self.__str__())
			siguiente += 1

	# Metodo que representa al objeto
	def __str__(self):
		temporal = "["
		for elemento in self.datos:
			temporal += " "+str(elemento)
		temporal += " ]\nNumero de iteraciones = "+str(self.iteraciones)
		return temporal
