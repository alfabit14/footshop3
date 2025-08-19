import tkinter as tk

root = tk.Tk()
root.geometry("400x400")
root.title("cadastro de alunos")

label_nome = tk.Label(root,text="Nome:")
label_nome.grid(row=0,column=0)
entry_nome=tk.Entry(root,width=45)
entry_nome.grid(row=0, column = 1)

label_ano = tk.Label(root,text="Ano:")
label_ano.grid(row=1,column=0)
entry_ano=tk.Entry(root,width=45)
entry_ano.grid(row=1, column = 1)

label_idade = tk.Label(root,text="Idade:")
label_idade.grid(row=2,column=0)
entry_idade=tk.Entry(root,width=45)
entry_idade.grid(row=2, column = 1)

button_cadastrar=tk.Button(root,text="cadastro")
button_cadastrar.grid(row=4, column=0)

button_nova_idade=tk.Button(root,text="atualizar idade")
button_nova_idade.grid(row=5, column=0)

button_novo_nome=tk.Button(root,text="atualizar nome")
button_novo_nome.grid(row=6, column=0)

listabox_aluno=tk.Listbox(root)
listabox_aluno.grid(row=8, column=1, columnspan=1) 

lista_aluno = []

def cadastrar():
    nome = entry_nome.get()
    ano = entry_ano.get()
    idade = int(entry_idade.get())
    aluno = {"nome":nome, "ano":ano, "idade":idade}
    lista_aluno.append (aluno)
    atualizar_lista_aluno()

def atualizar_nome():
    nome_antigo = listabox_aluno.get(tk.ACTIVE).split("-")[0]
    for indice_aluno,aluno in enumerate (lista_aluno):
        if aluno["nome"]== nome_antigo:
            nome_novo = entry_nome.get()
            lista_aluno[indice_aluno]["nome"] =nome_novo
            atualizar_lista_aluno()
            break

def atualizar_idade():
    idade_antiga = listabox_aluno.get(tk.ACTIVE).split("-")[0]
    for indice_aluno,idade in enumerate (lista_aluno):
        idade_nova = entry_idade.get()
        lista_aluno[indice_aluno]["idade"] = idade_nova
        atualizar_lista_aluno()
        break

def atualizar_lista_aluno():
    listabox_aluno.delete(0,tk.END)
    for aluno in lista_aluno:
        listabox_aluno.insert(tk.END,aluno["nome"] + "-" + aluno["ano"] + "-" + str(aluno["idade"]))

def inicializar():
    atualizar_lista_aluno()

inicializar()
button_cadastrar.config(command=cadastrar)
button_novo_nome.config(command=atualizar_nome)
button_nova_idade.config(command=atualizar_idade)

root.mainloop()
