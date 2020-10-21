from tkinter import *

janela = Tk()


def btSV_click():
    print(id_livro.get())
    print(id_aluno.get())


def btCN_click():
    print("Cancelar")


janela.title("Cadastrar Emprestimos")

id_livro = Entry(janela)
id_livro.place(x=150, y=200, width=200, height=30)
lbid_livro = Label(janela, text="Id do Livro:")
lbid_livro.place(x=20, y=200,)
lbid_livro.config(font="Arial 15 bold")

id_aluno = Entry(janela)
id_aluno.place(x=150, y=250, width=200, height=30)
lbid_aluno = Label(janela, text="Id do Aluno:")
lbid_aluno.place(x=20, y=250)
lbid_aluno.config(font="Arial 15 bold")

btSV = Button(janela, text="Salvar", command=btSV_click)
btSV.place(x=950, y=700, width=200, height=50)
btCN = Button(janela, width=20, text="Cancelar", command=btCN_click)
btCN.place(x=1150, y=700, width=200, height=50)

janela.geometry("1366x768+200+200")
janela.mainloop()
