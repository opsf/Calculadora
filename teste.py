import tkinter as tk

janela = tk.Tk()

count = 0
def criarNumero(numero):

    """
    Esta função cria o valor no Entry.
    :param valor: é o número que está no argumento da função lambda

    """
    e_entry.insert('end', numero)



def somar():
    global count
    count = count +1
    if count <= 1:
        global p
        p = int(e_entry.get())
        e_entry.delete(0, 'end')
        print(f'primeiro {p}')
    else:
        p = p + int(e_entry.get())
        e_entry.delete(0, 'end')
        e_entry.insert(0,p)
        e_entry.delete(0, 'end')
        print(f'segundo {p}')

def resultado():

    global p
    global count

    b = int(e_entry.get())
    e_entry.delete(0, 'end')
    print(f'valor de b em resultado é: {b}')
    p = p+b
    e_entry.insert(0,p)
    count = 0
    p=0


def limpar():
    e_entry.delete(0, 'end')
    global count
    global p
    count = 0
    p = 0






###### CRIAÇÃO DOS WIDTHY ##########

e_entry = tk.Entry(janela, borderwidth=10, width=50)
bt1 = tk.Button(janela, text = "1", width=13, pady=20, command=lambda: criarNumero(1))
bt2 = tk.Button(janela, text = "2", width=13, pady=20, command=lambda: criarNumero(2))
bt3 = tk.Button(janela, text = "3", width=13, pady=20, command=lambda: criarNumero(3))
bt4 = tk.Button(janela, text = "4", width=13, pady=20, command=lambda: criarNumero(4))
bt5 = tk.Button(janela, text = "5", width=13, pady=20, command=lambda: criarNumero(5))
bt6 = tk.Button(janela, text = "6", width=13, pady=20, command=lambda: criarNumero(6))
bt7 = tk.Button(janela, text = "7", width=13, pady=20, command=lambda: criarNumero(7))
bt8 = tk.Button(janela, text = "8", width=13, pady=20, command=lambda: criarNumero(8))
bt9 = tk.Button(janela, text = "9", width=13, pady=20, command=lambda: criarNumero(9))
bt0 = tk.Button(janela, text = "0", width=13, pady=20, command=lambda: criarNumero(0))
bt_igual = tk.Button(janela, text="=", width=13, pady=20, command= resultado)
bt_limpar = tk.Button(janela, text="LIMPAR", width=13, pady=20, command=limpar)
bt_soma = tk.Button(janela, text="+", width=13, pady=20, command=somar)


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
bt_limpar.grid(row=4,column= 1)
bt_igual.grid(row=4,column= 2)
bt_soma.grid(row=5,column=0)



janela.mainloop()
