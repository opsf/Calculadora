from tkinter import *
from tkinter import ttk



janela = Tk()

nome = StringVar()

###### CRIAÇÃO DOS WIDTHY ##########

e_entry = Entry(janela, borderwidth=5, width=50 )
bt1 = Button(janela, text = "1")
bt2 = Button(janela, text = "2")
bt3 = Button(janela, text = "3")
bt4 = Button(janela, text = "4")
bt5 = Button(janela, text = "5")
bt6 = Button(janela, text = "6")
bt7 = Button(janela, text = "7")
bt8 = Button(janela, text = "8")
bt9 = Button(janela, text = "9")
bt0 = Button(janela, text = "0")



###### LOCALIZAÇÃO DOS WIDTHY ######

e_entry.grid(row=0,column=0,columnspan=3)

bt1.grid(row=3, column=0)
bt2.grid(row=3, column=1)
bt3.grid(row=3, column=2)

bt4.grid(row=2, column=0)
bt5.grid(row=2, column=1)
bt6.grid(row=2, column=2)

bt7.grid(row=1, column=0)
bt8.grid(row=1, column=1)
bt9.grid(row=1, column=2)

bt0.grid(row=4, column=0)


janela.mainloop()
