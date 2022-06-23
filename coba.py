from forex_python.bitcoin import BtcConverter
import tkinter as tk
from tkinter import *
from tkinter import messagebox as msg 

root = Tk()

my_string_var = StringVar() 
name_var=tk.StringVar()
passw_var=tk.StringVar()



class crypto(tk.Tk):
    def __init__(self, *args,**kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)


        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont, ):
    
     self.name=name_var.get()
     self.password=passw_var.get()
     
     frame = self.frames[cont]
     frame.tkraise()

   


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Selamat datang di BTC to Currency conventer, silahkan masukan password", font=("Verdana", 16))
        label.pack(pady=1,padx=1)

        label1 = tk.Label(self, text="Nama", font=("Verdana", 13))
        label1.pack(pady=0,padx=100,ipadx=100)

        name = Entry(self, textvariable = name_var,)
        name.pack(pady=2, padx=1)

        label2 = tk.Label(self, text="Password", font=("Verdana", 13))
        label2.pack(pady=0,padx=100,ipadx=100)

        password = Entry(self,textvariable = passw_var, show = '*')
        password.pack(pady=3, padx=1)

        button1 = tk.Button(self, text="Submit",
                            command=lambda: controller.show_frame(PageOne))
        button1.pack()

  



class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two!!!", font=("Verdana",16))
        label.pack(pady=10,padx=10)


        label3=tk.Label(self, text='Men-Konversi dari BTC ke mata uang euro (EUR)')

        label3.pack(pady=10,padx=10)

        button3=tk.Button(self,text = 'BTC to EUR',
                            command=lambda: controller.eurbtc(parent, controller))
                            
        button3.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack(pady=10,padx=10)

    def eurbtc(self,parent, controller):
      
       b = BtcConverter()   
       hasilbtceur = b.get_latest_price('EUR') 
       label3=tk.Label(self, text=f'Hasil konversi{hasilbtceur}')
       label3.pack(pady=10,padx=10)



window = crypto()

window.mainloop()