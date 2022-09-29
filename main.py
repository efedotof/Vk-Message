#import
import sys
import os
from tkinter import *
from tkinter import ttk
import time
import threading
import win10toast
import selenium_botss
from start_bot import *
from selenium_botss import *

global polizovatel_times
global mission_componion

def callbackFunc(event):
    print("New Element Selected",time_dialog_Combobox.get())
    if time_dialog_Combobox.get() == '3600':
        polizovatel_times = selenium_botss.chasa
    if time_dialog_Combobox.get() == '5400':
        polizovatel_times = selenium_botss.poltora_chasa
    if time_dialog_Combobox.get() == '1800':
        polizovatel_times = selenium_botss.pol_chasa
    if time_dialog_Combobox.get() == '180':
        polizovatel_times = selenium_botss.three_minuts

def cycli(event):
    print(cycli_dialog_Combobox.get())

def no_butt():
    lms.destroy()

def yes_butt():
    lms.destroy()
    root.destroy()
    bot_starting()

def button_start():
    global lms
    lms = Tk()
    lms.title('Vk-сообщитель'), lms.geometry("130x100+450+150")
    kk = Label(lms,text="Вы сохранили данные \n перед запуском ?")
    kk.grid(row = 0, column= 0, sticky="w")
    yes_but = Button(lms,text="Да", height=1,width=2, command=yes_butt)
    no_but = Button(lms,text="Нет",height= 1, width=2, command=no_butt)
    yes_but.grid(row = 1, column= 0)
    no_but.grid(row = 2, column = 0)
    lms.mainloop()

def save_packing_file():
    with open('txt/login.txt', 'w', encoding='utf-8') as f:
        print(login.get(), file=f)
    with open('txt/password.txt', 'w', encoding='utf-8') as f:
        print(password.get(), file=f)
    with open('txt/link.txt', 'w', encoding='utf-8') as f:
        print(link.get(), file=f)
    with open('txt/message.txt', 'w', encoding='utf-8') as f:
        print(massahe.get(), file=f)
    with open('txt/miss_pol.txt', 'w', encoding='utf-8') as f:
        print(cycli_dialog_Combobox.get(), file=f)
    with open('txt/polizovatel_time.txt', 'w', encoding='utf-8') as f:
        print(time_dialog_Combobox.get(), file=f)
    os.execv(sys.argv[0], sys.argv)
def pact_tkinter():
    global timer_label, time_dialog_Combobox,selected_month,cycli_dialog_Combobox,login,password,link,massahe
    selected_month = StringVar()
    lbl = Label(root, height= 10, width= 40, text = "Добро пожаловать !")
    lbl.grid(row = 0,column= 0)
    login = StringVar()
    password = StringVar()
    link = StringVar()
    massahe = StringVar()


    name_label = Label(text="Login VK:")
    surname_label = Label(text="Pass VK:")
    name_mess_label = Label(text = "Link Dialog:")
    time_mess_label = Label(text = "Time Messag:")
    messages_label = Label(text = "Messages:")
    massage_cycle = Label(text = "num rep:")

    massage_cycle.grid(row=5,column=0,sticky="w")
    messages_label.grid(row = 6,column=0,sticky='w')
    name_label.grid(row=1, column=0, sticky="w")
    surname_label.grid(row=2, column=0, sticky="w")
    name_mess_label.grid(row = 3, column= 0,sticky="w")
    time_mess_label.grid(row= 4, column=0, sticky="w")


    but_start = Button(text="Start", height=1, width=10, command = button_start)
    but_save = Button(text='Save', height=1,width=10,command=save_packing_file)

    but_save.grid(row=8,column=0,padx=3,pady=3)
    but_start.grid(row= 9, column=0, padx= 3,pady=3)


    massage_entry = Entry(textvariable=massahe)
    name_entry = Entry(textvariable=login)
    surname_entry = Entry(textvariable=password)
    link_dialog = Entry(textvariable=link)


    time_dialog_Combobox = ttk.Combobox( width= 10, height=10, textvariable=selected_month)
    time_dialog_Combobox['values'] = ["3600","5400","1800", "180"]
    time_dialog_Combobox.current(0)
    time_dialog_Combobox.bind("<<ComboboxSelected>>", callbackFunc)

    cycli_dialog_Combobox = ttk.Combobox(width=10, height=10)
    cycli_dialog_Combobox['values'] = ["1","2","3", "4","5","6", "7","8","9","10"]
    cycli_dialog_Combobox.current(0)
    cycli_dialog_Combobox.bind("<<ComboboxSelected>>", cycli)

    massage_entry.grid(row=6,column=0,pady=5,padx=5)
    name_entry.grid(row=1, column=0, padx=5, pady=5)
    surname_entry.grid(row=2, column=0, padx=10, pady=10)
    link_dialog.grid(row = 3, column=0, padx=10, pady=10)


    time_dialog_Combobox.grid(row = 4, column = 0, padx = 5,pady = 5)
    cycli_dialog_Combobox.grid(row = 5, column = 0, padx = 5,pady = 5)
def tkinter_main():
    global root
    root = Tk()
    root.title('Vk-сообщитель'), root.geometry("300x410+450+150"), pact_tkinter(), root.mainloop()

if __name__=='__main__':
    tkinter_main()