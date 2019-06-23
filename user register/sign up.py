#!/usr/bin/python3

from tkinter import *
from tkinter import messagebox

import time
import sqlite3


meConexion = sqlite3.connect('users')
meCursor = meConexion.cursor()

# ----------------

# meCursor.execute( '''CREATE TABLE USERS (
# 					ID INTEGER PRIMARY KEY AUTOINCREMENT,
# 					NAME VARCHAR(50) UNIQUE,
# 					EMAIL VARCHAR(50) UNIQUE,
# 					PASSWORD VARCHAR(50) UNIQUE,
# 					GENDER INTEGER,
# 					ACTIVE BOOL)''')
# # ------------------

root = Tk()
root.resizable(width=False, height=False)
root.title('User Register')


GREEN = '#22dd99'
RED = '#e63569'
BG = 'white'



#-------Test query select email --------
#EMAIL = 'hugomontaez@gmail.com'
#query = f"""SELECT EMAIL FROM USERS WHERE EMAIL = '{EMAIL}' """
#meCursor.execute(query)



class Aplication():
	def __init__(self):	

		# ------------PICTURE------------
		miPicture = Frame(root,width = 300,height = 760)
		miPicture.configure(bg = BG)
		miPicture.pack()

		picture = PhotoImage(file = 'src/icono.png')
		#image = Label(miFrame,image = picture)
		image = Button(miPicture,image = picture,command = self.infoAdicional )
		image.grid(row = 0,column = 1,padx = 85,pady = 10)

		# -------------------------
		
		miFrame = Frame(root,width = 300,height = 760)
		miFrame.configure(bg = BG)
		miFrame.pack()

		self.meName = StringVar()
		self.meEmail = StringVar()
		self.mePassword = StringVar()

		#YEAR/MONTH/DAY
		self.date = time.strftime('%d/%m/%y')
		self.gender = IntVar()



		# -----------Entry-----------
		cuadroName = Entry(miFrame,textvariable = self.meName)
		cuadroName.grid(row = 1, column = 1,padx = 10,pady = 10)

		cuadroEmail = Entry(miFrame,textvariable = self.meEmail)
		cuadroEmail.grid(row = 2, column = 1,padx = 10,pady = 10)

		cuadroPassword = Entry(miFrame,textvariable = self.mePassword)
		cuadroPassword.grid(row = 3, column = 1,padx = 10,pady = 10)
		cuadroPassword.config(show = '*')

		#----------Label----------

		nombreLabel = Label(miFrame,text = 'Name:')
		nombreLabel.grid( row = 1 ,column = 0,sticky = 'w',padx = 10,pady = 10)

		EmailLabel = Label(miFrame,text = 'Email:')
		EmailLabel.grid( row = 2 ,column = 0,sticky = 'w',padx = 10,pady = 10)

		passwordLabel = Label(miFrame,text = 'Password:')
		passwordLabel.grid( row = 3 ,column = 0,sticky = 'w',padx = 10,pady = 10)

		dateLabel = Label(miFrame,text = 'Date:')
		dateLabel.grid( row = 4 ,column = 0,sticky = 'w',padx = 10,pady = 10)

		dateLabel = Label(miFrame,text = str(self.date))
		dateLabel.config(bg = GREEN)
		dateLabel.grid( row = 4 ,column = 1,sticky = 'w',padx = 10,pady = 10)
	
		comentarioGender = Label(miFrame,text = 'Gender:')		
		comentarioGender.grid( row = 5 ,column = 0,sticky = 'w',padx = 10,pady = 10)		


		#--------RADIOBUTTON-------
		genderM = Radiobutton(miFrame,text = 'Male', variable = self.gender,value = 1)
		genderF = Radiobutton(miFrame,text = 'Female', variable = self.gender, value = 2)
		genderE = Radiobutton(miFrame,text = 'No binary', variable = self.gender, value = 3)

		genderM.config(bg = BG)		
		genderF.config(bg = BG)		
		genderE.config(bg = BG)		

		genderM.grid(row = 5, column = 1,sticky = 'w',padx = 10,pady = 10)
		genderF.grid(row = 6, column = 1,sticky = 'w',padx = 10,pady = 10)
		genderE.grid(row = 7,column = 1,sticky = 'w', padx = 10,pady = 10)


		#-----------form----------
		
		miform = Frame(root,width = 300,height = 760)
		miform.configure(bg = BG)
		miform.pack()

		#-----------Alert---------

		self.alertNombre = Label(miFrame)
		self.alertNombre.config(bg = BG)
		self.alertNombre.grid(row = 8 ,column = 1,sticky = 'w',padx = 10,pady = 10)


		#-------Envio y comprobar datos--------

		botonSend = Button(miform,text = 'Send',command = self.enviar,bg = GREEN)
		botonExit = Button(miform,text = 'Exit',command = self.quit, bg = RED)

		botonSend.grid(row = 8,column = 2,sticky = 'w',padx = 40,pady = 10)
		botonExit.grid(row = 8,column = 0,sticky = 'w',padx = 40,pady = 10)

		self.update()


	def infoAdicional(self):
		messagebox.showinfo('Register User', 'Developer Hug58 \nTwitter: hug588 \nGithub: hug58')


	def comprobarInfo(self):
		enviar = 1

		nombre = self.meName.get()
		password = self.mePassword.get()
		correo = self.meEmail.get() 		
		gender = self.gender.get()

		infoUsuario = (nombre,correo,password,gender,1,self.date)

		if  nombre == '':
			enviar = 0

		if  password == '':
			enviar = 0
			
		if correo == '':
			enviar = 0
		
		elif correo.find('@') < 0:			
			enviar = 0

		if gender <= 0:
			enviar = 0

		if enviar == 1:
			self.meName.set('')
			self.mePassword.set('')
			self.meEmail.set('') 		
			self.gender.set(0)
			return infoUsuario
		else:
			return 0


	def comprobar_db(self,email):
		meCursor.execute(f"""SELECT EMAIL FROM USERS WHERE EMAIL == '{email}'""") 
		respuesta = meCursor.fetchall()

		if respuesta:
			return 0
		else:
			return 1 


	def enviar(self):
		infoUsuario = self.comprobarInfo()

		if  infoUsuario != 0:
			email = infoUsuario[1]
	
			if self.comprobar_db(email) == 1:
				self.insert(infoUsuario)
				self.alertNombre.config(bg = GREEN,text = 'Registered')
			else:
				self.alertNombre.config(bg = RED,text = 'Email already used')

		else:
			self.alertNombre.config(bg = RED,text = 'Incomplete data') 

	
	def insert(self,values):
		meCursor.execute("""INSERT INTO USERS VALUES(NULL,?,?,?,?,?,?)""",values)
		meConexion.commit()


	def quit(self):
		meConexion.close()
		quit()


	def update(self):
		root.mainloop()

if __name__ == '__main__':
	app = Aplication()

	