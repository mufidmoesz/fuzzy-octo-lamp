
def submit():
 
    name=name_var.get()
    password=passw_var.get()
     
    print("The name: " + name)
    print("The password : " + password)
   

def eurbtc():
         
          b = BtcConverter()   
          hasileurbtc=b.get_latest_price('EUR') 
          Label(window2, text=f"Hasil Konveri BTC ke EUR adalah sebesar €:{hasileurbtc}").grid(row=3, column = 3)

def usdbtc():
     b = BtcConverter()   
     b.get_latest_price('USD')  

def idrbtc():
     b = BtcConverter()   
     b.get_latest_price('IDR')       
 

    
     

from forex_python.bitcoin import BtcConverter
import tkinter as tk
from tkinter import *
from tkinter import messagebox as msg 

window1 = tk.Tk()

my_string_var = StringVar() 




window1.title('Login BTC Conventer')
window1.geometry("600x400")

frame = Frame(window1)
frame.grid()

name_var=tk.StringVar()
passw_var=tk.StringVar()

   

Label(window1, text ='Selamat datang di Progam BTC to Currency Conventer').grid(row=0,column=2)
Label(window1, text ='Silahkan masukan nama dan password').grid(row=1,column=2)
Label(window1, text='Name').grid(row=2)
Label(window1, text='pass').grid(row=3)

nama = Entry(window1, textvariable = name_var,)
nama.grid(row=2, column=1)

password = Entry(window1,textvariable = passw_var, show = '*')
password.grid(row=3, column=1)

keluar = tk.Button(window1,text = 'Keluar', fg ='red',command=window1.destroy).grid(row=20 , column = 20)
submitt = tk.Button(window1, text ='Submit', fg = 'blue',command=submit).grid(row=20, column = 1)



if password == "123":
        
     window2 = tk.Toplevel(window1)

     window2.title('BTC Conventer')
     window2.geometry("600x400")
     Label(window2, text='Silahkan pilih menu yang tersedia').grid(row=0, column = 3)
     Label(window2, text='Men-Konversi dari BTC ke mata uang euro (EUR)').grid(row=1)
     tk.Button(window2,text = 'BTC to EUR',command=eurbtc).grid(row=2 , column = 0)
     




     k=tk.Button(window2,text = 'Keluar', fg ='red',command=window2.destroy).grid(row=20 , column = 20)
     window2.mainloop()



     
elif password != "123":
      msg.showwarning("Peringatan", "Password Salah") 

          
window1.mainloop()

 
 
 
