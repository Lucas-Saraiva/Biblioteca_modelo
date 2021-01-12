from tkinter import *


def btSV_click():
    print(nome.get())
    print(genero.get())
    print(autora.get())
    print(editora.get())


def btCN_click():
    exit()


janela = Tk()

janela.title("Cadastro de Livro")

nome = Entry(janela)
nome.place(x=120, y=200)
lbnome = Label(janela, text="Nome do Livro:")
lbnome.place(x=20, y=200)

genero = Entry(janela)
genero.place(x=122, y=250)
lbgenero = Label(janela, text="Genero do Livro:")
lbgenero.place(x=14, y=250)

autora = Entry(janela)
autora.place(x=120, y=300)
lbautora = Label(janela, text="Autora do Livro:")
lbautora.place(x=16, y=300)

editora = Entry(janela)
editora.place(x=120, y=350)
lbeditora = Label(janela, text="Editora do Livro:")
lbeditora.place(x=13, y=350)

btSV = Button(janela, text="Salvar", command=btSV_click)
btSV.place(x=950, y=650, width=200, height=50)
btCN = Button(janela, text="Cancelar", command=btCN_click)
btCN.place(x=1150, y=650, width=200, height=50)

janela.geometry("1366x768+200+200")
janela.mainloop()
