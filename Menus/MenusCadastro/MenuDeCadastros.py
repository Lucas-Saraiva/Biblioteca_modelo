from tkinter import *


def button_cadastro_livro():
    print("button_cadastro_livro")


def button_cadastro_aluno():
    print("button_cadastro_aluno")


def button_cadastro_emprestimo():
    print("button_cadastro_emprestimo")


janela = Tk()

janela.title("Cadastros")

bt1 = Button(janela, text="Cadastrar Livro", command=button_cadastro_livro)
bt1.place(x=200, y=500, width=300, height=50)
bt2 = Button(janela, text="Cadastrar Aluno", command=button_cadastro_aluno)
bt2.place(x=500, y=500, width=300, height=50)
bt3 = Button(janela, text="Cadastrar Emprestimo", command=button_cadastro_emprestimo)
bt3.place(x=800, y=500, width=300, height=50)

janela.geometry("1366x768+200+200")
janela.mainloop()
