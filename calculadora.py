from tkinter import *

raiz = Tk()

miFrame = Frame(raiz)
miFrame.pack()


#PANTALLA------


NumPantalla = StringVar()

class Aplication():
	



	def __init__(self):

		self.pantalla = Entry(miFrame,textvariable = NumPantalla)
		self.pantalla.grid(row = 1,column= 1, padx = 10,pady = 10,columnspan = 4)
		self.pantalla.config(background = "black",fg = "#FCF404",justify = "right")


		self.simbolos = "789/456X123-0.=+"
		self.simbolos = list(self.simbolos)

		self.f = 2
		self.j = 1
		self.bottons = []

		self.num1 = 0
		self.num2 = 0
		self.operador = ""

	def botton(self):
		x = None
		for i in range(len(self.simbolos)):

			x = Button(miFrame,text = self.simbolos[i],width = 4)
			self.bottons.append(x)
			

		for i in self.bottons:
			i.grid(row = self.f, column = self.j)
			
			if self.j < 4:
				self.j +=1
			else:
				self.f +=1
				self.j = 1


		#for i in range(len(self.bottons)):
		#	self.bottons[i].config(command = lambda:self.mostrar(self.simbolos[i]))


		self.bottons[0].config(command = lambda:self.mostrar(self.simbolos[0]))
		self.bottons[1].config(command = lambda:self.mostrar(self.simbolos[1]))
		self.bottons[2].config(command = lambda:self.mostrar(self.simbolos[2]))
		self.bottons[3].config(command = lambda:self.operacion_new(self.simbolos[3]))
		self.bottons[4].config(command = lambda:self.mostrar(self.simbolos[4]))
		self.bottons[5].config(command = lambda:self.mostrar(self.simbolos[5]))
		self.bottons[6].config(command = lambda:self.mostrar(self.simbolos[6]))
		self.bottons[7].config(command = lambda:self.operacion_new(self.simbolos[7]))
		self.bottons[8].config(command = lambda:self.mostrar(self.simbolos[8]))
		self.bottons[9].config(command = lambda:self.mostrar(self.simbolos[9]))
		self.bottons[10].config(command = lambda:self.mostrar(self.simbolos[10]))
		self.bottons[11].config(command = lambda:self.operacion_new(self.simbolos[11]))
		self.bottons[12].config(command = lambda:self.mostrar(self.simbolos[12]))
		self.bottons[13].config(command = lambda:self.mostrar(self.simbolos[13]))
		self.bottons[14].config(command = lambda:self.operacion_new(self.simbolos[14]))
		self.bottons[15].config(command = lambda:self.operacion_new(self.simbolos[15]))

	def mostrar(self,num):
		if NumPantalla.get() != "0":
			NumPantalla.set(NumPantalla.get()+num)
		else:
			NumPantalla.pantalla.set(num)

	def operacion(self):
		resultado = 0
		num1 = 0
		num2 = 0
		cadena = NumPantalla.get()
		subcadena = ""
		for i in range(len(cadena)):

			if cadena[i] == ".":
				for j in cadena[i+1:]:
					subcadena +=j 
					if j =="+" or j =="-" or j =="*" or j =="/":
						
						num1 = cadena[:i+len(subcadena)] 
						
						num1 = float(num1)
						#print(type(num1)) 
						break
						#num1 = cadena[:i] + cadena[:j]
						#num1 = float(num1) 
						#print(num1)



			if cadena[i] == "X":
				num1 = int(cadena[:i])
				num2 = int(cadena[i+1:])
				resultado = num1*num2
			elif cadena[i] == "/":
				num1 = int(cadena[:i])
				num2 = int(cadena[i+1:])
				resultado = num1 / num2

			elif cadena[i] == "+":
				num1 = int(cadena[:i])
				num2 = int(cadena[i+1:])
				resultado = num1 +num2
		
		
		NumPantalla.set(str(resultado))
		#NumPantalla.set(str(resultado))


	def operacion_new(self,simbolos):
		resultado = 0

		
		if simbolos == "=":
			self.num2 = int(NumPantalla.get())
			print(self.num2)
			#print(self.num1)

			if self.operador == "+":
				resultado = self.num1 + self.num2
			
			elif self.operador == "-":
				resultado = self.num1 - self.num2

			elif self.operador == "X":
				resultado = self.num1 * self.num2

			elif self.operador == "/":
				resultado = self.num1/self.num2

			NumPantalla.set(str(resultado))

		elif simbolos == "+":
			self.num1 = int(NumPantalla.get())
			self.operador = "+"
			NumPantalla.set("")

		elif simbolos == "-":
			self.num1 = int(NumPantalla.get())
			self.operador = "-"
			NumPantalla.set("")

		elif simbolos == "X":
			self.num1 = int(NumPantalla.get())
			self.operador = "X"
			NumPantalla.set("")

		elif simbolos == "/":
			self.num1 = int(NumPantalla.get())
			self.operador = "/"
			NumPantalla.set("")


	def update(self):
		ap.botton()

		raiz.mainloop()



ap = Aplication()

ap.update()
