from tkinter import *


def btSV_click():
    print(nome.get())
    print(turma.get())


def btCN_click():
    print("Cancelar")


janela = Tk()


nome = Entry(janela)
nome.place(x=120, y=200, width=200, height=30)
lbnome = Label(janela, text="Nome do Aluno:")
lbnome.place(x=12, y=200)

turma = Entry(janela)
turma.place(x=120, y=250, width=200, height=30)
lbturma = Label(janela, text="Turma do Aluno:")
lbturma.place(x=11, y=250)

btSV = Button(janela, text="Salvar", command=btSV_click)
btSV.place(x=900, y=650, width=200, height=50)
btCN = Button(janela, text="Cancelar", command=btCN_click)
btCN.place(x=1100, y=650, width=200, height=50)

janela.title("Cadastrar Aluno")
janela.geometry("1366x768+200+200")
janela.mainloop()
