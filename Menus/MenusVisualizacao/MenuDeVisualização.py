from tkinter import *

def button_visualizar_livro():
    print("button_visualizar_livro")


def button_visualizar_aluno():
    print("button_visualizar_aluno")


def button_visualizar_emprestimo():
    print("button_visualizar_emprestimo")


janela = Tk()

janela.title("Visualizar")

bt1 = Button(janela, width=20, text="Visualizar Livros", command=button_visualizar_livro)
bt1.place(x=200, y=350)
bt2 = Button(janela, width=20, text="Visualizar Alunos", command=button_visualizar_aluno)
bt2.place(x=400, y=350)
bt3 = Button(janela, width=20, text="Visualizar Emprestimos", command=button_visualizar_emprestimo())
bt3.place(x=600, y=350)


janela.geometry("1000x500+200+200")
janela.mainloop()
