from forex_python.bitcoin import BtcConverter
import tkinter as tk
from tkinter import *
from tkinter import messagebox as msg 


#Window
window1 = tk.Tk()

window1.title('BTC Conventer')
window1.geometry("750x800")


#String_Var
my_string_var1 = StringVar()

nominaleur=tk.StringVar()
nominalusd=tk.StringVar()
nominalidr=tk.StringVar()

nominaleur1=tk.StringVar()
nominalusd1=tk.StringVar()
nominalidr1=tk.StringVar()

#Frame
frame = Frame(window1)
frame.grid()


#FUNGSI 1 koin BTC ke mata uang

def eurbtc():
     b = BtcConverter()   
     hasileurbtc=b.get_latest_price('EUR') 
     my_string_var1.set(f"Hasil Konveri ฿1 BTC ke EUR adalah sebesar :€{hasileurbtc}")

def usdbtc():
     b = BtcConverter()   
     hasilusdbtc=b.get_latest_price('USD') 
     my_string_var1.set(f"Hasil Konveri ฿1 BTC ke USD adalah sebesar :${hasilusdbtc}")


def idrbtc():
     b = BtcConverter()   
     hasilidrbtc=b.get_latest_price('IDR') 
     my_string_var1.set(f"Hasil Konveri ฿1 BTC ke IDR adalah sebesar :Rp.{hasilidrbtc}")


#FUNGSI Nominal koin BTC ke mata uang

def submiteur():
     b = BtcConverter()
     hasileur=nominaleur.get()
     totaleur = b.convert_btc_to_cur(float(hasileur), 'EUR')
     my_string_var1.set(f"Hasil Konversi ฿{hasileur} BTC ke EUR adalah sebesar :€{totaleur}")


def submitusd():
     b = BtcConverter()
     hasilusd=nominalusd.get()
     totalusd = b.convert_btc_to_cur(float(hasilusd), 'USD')
     my_string_var1.set(f"Hasil Konveri ฿{hasilusd} BTC ke USD adalah sebesar :${totalusd}")

def submitidr():
     b = BtcConverter()
     hasilidr =nominalidr.get()
     totalidr = b.convert_btc_to_cur(float(hasilidr), 'IDR')
     my_string_var1.set(f"Hasil Konveri ฿{hasilidr} BTC ke USD adalah sebesar :Rp.{totalidr}")
    


def eurbtc_cur():

     Entry(window1, textvariable = nominaleur,).grid(row=17, column=1)
     tk.Button(window1, text ='Submit', fg = 'blue',command=submiteur).grid(row=20, column = 1)

def usdbtc_cur():

     Entry(window1, textvariable = nominalusd,).grid(row=17, column=1)
     tk.Button(window1, text ='Submit', fg = 'blue',command=submitusd).grid(row=20, column = 1)

def idrbtc_cur():

     Entry(window1, textvariable = nominalidr,).grid(row=17, column=1)
     tk.Button(window1, text ='Submit', fg = 'blue',command=submitidr).grid(row=20, column = 1)



#FUNGSI Mata uang ke koin BTC

try:
 def submiteur1():
     b = BtcConverter()
     hasileur1 = nominaleur1.get()
     totaleur1 = b.convert_to_btc(float(hasileur1), 'EUR')
     my_string_var1.set(f"Hasil Konversi €{hasileur1} EUR ke ke BTC adalah sebesar ฿.{totaleur1}")

 def submitusd1():
     b = BtcConverter()
     hasilusd1 = nominalusd1.get()
     totalusd1 = b.convert_to_btc(float(hasilusd1), 'USD')
     my_string_var1.set(f"Hasil Konversi €{hasilusd1} EUR ke ke BTC adalah sebesar ฿.{totalusd1}")


 def submitidr1():
     b = BtcConverter()
     hasilidr1 = nominalidr1.get()
     totalidr1 = b.convert_to_btc(float(hasilidr1), 'IDR')
     my_string_var1.set(f"Hasil Konversi {hasilidr1} EUR ke ke BTC adalah sebesar ฿.{totalidr1}")


except ValueError:
     msg.showwarning("Peringatan", "PROGAM HANYA MENGGUNAKAN ANGKA SAJA") 
     
     




def btceur_cur():
     Entry(window1, textvariable = nominaleur1,).grid(row=17, column=2)
     tk.Button(window1, text ='Submit', fg = 'blue',command=submiteur1).grid(row=20, column = 2)

def btcusd_cur():
     Entry(window1, textvariable = nominalusd1,).grid(row=17, column=2)
     tk.Button(window1, text ='Submit', fg = 'blue',command=submitusd1).grid(row=20, column = 2)

def btcidr_cur():
     Entry(window1, textvariable = nominalidr1,).grid(row=17, column=2)
     tk.Button(window1, text ='Submit', fg = 'blue',command=submitidr1).grid(row=20, column = 2)


 


#LABEL
Label(window1, text='Silahkan pilih menu yang tersedia', font=('Helvetica', 14)).grid(row=0, column = 1, pady=4)
Label(window1, text='Men-Konversi dari 1 koin BTC ke Berbagai mata uang (USD, EUR, IDR)', font=('Helvetica', 14)).grid(row=1, column=1, pady=4)
Label(window1, text='Men-Konversi dari Nominal koin BTC ke Berbagai mata uang (USD, EUR, IDR)', font=('Helvetica', 14)).grid(row=6, column=1, pady=4)
Label(window1, text='Men-Konversi dari Berbagai mata uang (USD, EUR, IDR) ke Koin BTC ', font=('Helvetica', 14)).grid(row=11, column=1, pady=4)


my_label1 = Label(window1,textvariable = my_string_var1, font=('Helvetica', 14)).grid(row=21, column = 1)
my_string_var1.set("HASIL DATA AKAN DITAMPILKAN DISINI")


#BUTTON
tk.Button(window1,text = 'BTC(฿) to EUR(€)', font=('Helvetica', 14), command=eurbtc).grid(row=2 , column = 1, pady=4)
tk.Button(window1,text = 'BTC(฿) to USD($)', font=('Helvetica', 14),command=usdbtc).grid(row=3 , column = 1, pady=4)
tk.Button(window1,text = 'BTC(฿) to IDR(Rp)', font=('Helvetica', 14),command=idrbtc).grid(row=4 , column = 1, pady=4)

tk.Button(window1,text = 'Nominal BTC(฿) to EUR(€)', font=('Helvetica', 14),command=eurbtc_cur).grid(row=7, column = 1, pady=4)
tk.Button(window1,text = 'Nominal BTC(฿) to USD($)', font=('Helvetica', 14),command=usdbtc_cur).grid(row=8, column = 1, pady=4)
tk.Button(window1,text = 'Nominal BTC(฿) to IDR(Rp)', font=('Helvetica', 14),command=idrbtc_cur).grid(row=9 , column = 1, pady=4)

tk.Button(window1,text = 'Nominal EUR(€) to BTC(฿)', font=('Helvetica', 14),command=btceur_cur).grid(row=12 , column = 1, pady=4)
tk.Button(window1,text = 'Nominal USD($) to BTC(฿)', font=('Helvetica', 14),command=btcusd_cur).grid(row=13 , column = 1, pady=4)
tk.Button(window1,text = 'Nominal IDR(Rp) to BTC(฿)', font=('Helvetica', 14),command=btcidr_cur).grid(row=14 , column = 1, pady=4)




keluar = tk.Button(window1,text = 'Keluar', fg ='red',command=window1.destroy).grid(row=20 , column = 20)

window1.mainloop() 


     

     


     




 

 
 
 
