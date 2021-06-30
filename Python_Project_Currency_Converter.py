# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 15:18:26 2021

@author: himan
"""

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from forex_python.converter import CurrencyRates

c = CurrencyRates()

root = Tk()
root.title("Currency Converter")
root.geometry("500x600")

a = ['USD', 'INR', 'EUR', 'JPY', 'BGN', 'CZK', 'DKK', 'GBP', 'HUF', 'PLN', 'RON', 'SEK', 
     'CHF', 'ISK', 'NOK', 'HRK', 'RUB', 'TRY', 'AUD', 'BRL', 'CAD', 'CNY', 'HKD', 'IDR', 
     'INR', 'KRW', 'MXN', 'MYR', 'NZD', 'PHP', 'SGD', 'THB', 'ZAR']

myNotebook = ttk.Notebook(root)
myNotebook.pack(pady=5)

def clear():
    amount_entry.delete(0,END)
    converted_entry.delete(0,END)
    
    
def convert():
    curr = c.convert(menu_select1.get(), menu_select2.get(), float(amount_entry.get()))
    curr = '{:,}'.format(round(curr,2))
    converted_entry.insert(0,curr)   


home = LabelFrame(root,text= "Currency to Convert")
home.pack(pady=20)


menu_select1 = StringVar(root)
menu_select1.set("USD")

drop1 = OptionMenu(home,menu_select1,*a)
drop1.pack(pady=10,padx=160)


conversion = LabelFrame(root,text="Conversion Currency")
conversion.pack(pady=20)

menu_select2 = StringVar(root)
menu_select2.set("USD")

drop2 = OptionMenu(conversion,menu_select2,*a)
drop2.pack(pady=10,padx=160)


amount_label = LabelFrame(root,text = "Amount to Convert")
amount_label.pack(pady=20)

amount_entry = Entry(amount_label,font =("Helvetica",24) )
amount_entry.pack(pady=10,padx=10)

convert_button = Button(amount_label,text="Convert",command = convert)
convert_button.pack(pady=20)

converted_label = LabelFrame(root,text = "Converted Currency")
converted_label.pack(pady=20)

converted_entry = Entry(converted_label,font = ("Helvetica",24),bg= "systembuttonface")
converted_entry.pack(padx=10,pady=10)

clear_button = Button(root,text = "Clear",command = clear)
clear_button.pack(pady=20)

space = Label(root,text="",width = 68)
space.pack()


root.mainloop()


