from tkinter import *


def button_visualizar():
    print("button_visualizar")


def button_cadastrar():
    print("button_cadastrar")


janela = Tk()

janela.title("Biblioteca")

bt1 = Button(janela, text="Cadastrar", command=button_cadastrar)
bt1.place(x=650, y=500, width=300, height=50)
bt1.config(font="Arial 15 bold")
bt2 = Button(janela, text="Visualizar", command=button_visualizar)
bt2.place(x=350, y=500, width=300, height=50)
bt2.config(font="Arial 15 bold")

janela.geometry("1366x768+200+200")
janela.mainloop()
