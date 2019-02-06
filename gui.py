import tkinter as tk

raiz = tk.Tk()
raiz.title("GUI BBDD ")




class Aplication():
    def __init__(self):
        form = tk.Frame(raiz,width = 300,height = 200)
        form.configure()
        form.pack()
        
        self.name = tk.StringVar()
        self.price = tk.StringVar()

        self.label_name = tk.Label(form,text = "NAME",width = 10,pady = 10)
        self.label_name.grid(row = 0,column = 0)
        
        self.entry_name = tk.Entry(form,width = 20,textvariable = self.name )
        self.entry_name.grid(row = 0,column = 1)
        
        self.label_price = tk.Label(form,text = "PRICE",width = 10,pady = 10)
        self.label_price.grid(row = 1,column = 0)

        self.entry_price = tk.Entry(form,width = 20,textvariable = self.price)
        self.entry_price.grid(row = 1,column = 1)


        miFrame = tk.Frame(raiz)
        miFrame.config(width = 1000,height = 600)
        miFrame.pack()


        self.label_name_list = tk.Label(miFrame,text = "NAME",width = 40)
        self.label_name_list.grid(row = 2,column = 0)    
        self.label_price_list = tk.Label(miFrame,text = "PRICE",width = 40)
        self.label_price_list.grid(row = 2,column = 1)
        
        self.elemento = tk.StringVar()

        self.listbox_name = tk.Listbox(miFrame,width = 42,listvariable = self.elemento,selectmode = tk.EXTENDED)
        self.listbox_name.grid(row = 3,column = 0)
        self.listbox_price = tk.Listbox(miFrame,width = 42)
        self.listbox_price.grid(row = 3,column = 1)
        
        self.button_new = tk.Button(miFrame,text = "New",command = self.insert,width= 40)
        self.button_new.grid(row = 4,column = 0)
        self.button_delete = tk.Button(miFrame,text = "Delete",width = 40,command = self.delete)
        self.button_delete.grid(row = 4,column = 1)


    def delete(self):
        seleccion_name = self.listbox_name.curselection()
        for i in seleccion_name:
            self.listbox_name.delete(i)
        
        seleccion_price = self.listbox_price.curselection()
        for i in seleccion_price:
            self.listbox_price.delete(i)



    def insert(self):
        self.listbox_name.insert(0,self.name.get())
        self.listbox_price.insert(0,self.price.get())


    def update(self):
        self.insert()
        self.elemento.get()
       
        raiz.mainloop()   

ap = Aplication()
ap.update()