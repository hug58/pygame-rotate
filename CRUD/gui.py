#!usr/bin/python3

import tkinter as tk
import sqlite3

miConexion = sqlite3.connect("Productos")
miCursor = miConexion.cursor()

raiz = tk.Tk()
raiz.title("GUI BBDD ")
raiz.resizable(width=False, height=False)

#try:
#
#except:
#    miCursor.execute( '''CREATE TABLE PRODUCTOS (
#    ID INTEGER PRIMARY KEY AUTOINCREMENT,
#    NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
#    PRECIO INTEGER
#    )
#''')



class Aplication():
	def __init__(self):
		form = tk.Frame(raiz,width = 300,height = 200)
		form.pack()
		
		miFrame = tk.Frame(raiz,width = 1000,height = 600)
		miFrame.pack()

		miCursor.execute("SELECT * FROM PRODUCTOS")
		self.variosProductos = miCursor.fetchall()
	
		self.product_name = [producto[1] for producto in self.variosProductos]
		self.product_price = [producto[2] for producto in self.variosProductos] 
		

		self.name = tk.StringVar()
		self.price = tk.IntVar()

		self.label_name = tk.Label(form,text = "NAME",width = 10,pady = 10)
		self.label_name.grid(row = 0,column = 0)
		
		self.entry_name = tk.Entry(form,width = 20,textvariable = self.name )
		self.entry_name.grid(row = 0,column = 1)
		
		self.label_price = tk.Label(form,text = "PRICE",width = 10,pady = 10)
		self.label_price.grid(row = 1,column = 0)

		self.entry_price = tk.Entry(form,width = 20,textvariable = self.price)
		self.entry_price.grid(row = 1,column = 1)



		#----------LIST NAME---------
		self.label_name_list = tk.Label(miFrame,text = "NAME")
		self.label_name_list.grid(row = 2,column = 0)    
		self.label_price_list = tk.Label(miFrame,text = "PRICE")
		self.label_price_list.grid(row = 2,column = 1)
		
		self.elements_name = tk.StringVar(value= self.product_name)
		self.elements_price = tk.StringVar(value= self.product_price)
		
		#---------LIST----------
		self.listbox_name = tk.Listbox(miFrame,width = 42,
		listvariable = self.elements_name,selectmode = tk.EXTENDED, bg = 'beige')
		self.listbox_name.grid(row = 3,column = 0)
		
		self.listbox_price = tk.Listbox(miFrame,width = 42, 
		listvariable = self.elements_price, bg = 'beige')
		self.listbox_price.grid(row = 3,column = 1)
		
		
		#----------BUTON----------
		self.button_new = tk.Button(miFrame,text = "New/Edit",command = self.insert,width= 40)
		self.button_new.grid(row = 4,column = 0)

		self.button_delete = tk.Button(miFrame,text = "Delete",command = self.delete,width = 40)
		self.button_delete.grid(row = 4,column = 1)


	def delete(self):
		seleccion_name = self.listbox_name.curselection()
		seleccion_price = self.listbox_price.curselection()
		
		for i in seleccion_name:
			values =str(self.variosProductos[i][0])
			
			miCursor.execute("DELETE FROM PRODUCTOS WHERE ID = {} ".format(values))

		for i in seleccion_price:
			miCursor.execute("DELETE FROM PRODUCTOS WHERE ID = {}".format(values))

				
		miCursor.execute("SELECT * FROM PRODUCTOS")

		self.variosProductos = miCursor.fetchall()
		self.elements_name.set([producto[1] for producto in self.variosProductos])
		self.elements_price.set([producto[2] for producto in self.variosProductos])
	


	def insert(self):
		if self.name.get() != "" and self.price.get() > 0:
			elemento = False
			for producto in self.variosProductos:
				if producto[1] == self.name.get():
					#print("YA TIENE ESTE ELEMENTO REGISTRADO, SI DESEA CAMBIAR EL PRECIO PULSA 'EDITAR' ")
					self.edit()
					elemento = True

			if elemento == False:
				values = (self.name.get(),self.price.get())
				miCursor.execute("INSERT INTO PRODUCTOS VALUES(NULL,?,?)",values)        
				miCursor.execute("SELECT * FROM PRODUCTOS")
				self.variosProductos = miCursor.fetchall()
				self.elements_name.set([producto[1] for producto in self.variosProductos])
				self.elements_price.set([producto[2] for producto in self.variosProductos])

		self.name.set("")
		self.price.set(0)

	def edit(self):
		update = (self.price.get(),self.name.get())
		miCursor.execute("UPDATE PRODUCTOS SET PRECIO = ? WHERE NOMBRE_ARTICULO = ?",update)

		miCursor.execute("SELECT * FROM PRODUCTOS")
		self.variosProductos = miCursor.fetchall()
		self.elements_name.set([producto[1] for producto in self.variosProductos])
		self.elements_price.set([producto[2] for producto in self.variosProductos])

	def update(self):
		raiz.mainloop()   


if __name__ == '__main__':
	app = Aplication()
	app.update()
	miConexion.commit()
	miConexion.close()
