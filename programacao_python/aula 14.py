import tkinter as tk
import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "estoque2"
)
cursor = conn.cursor()

def cadastrar():
    nome_produto = entry_nome.get()
    quantidade_produto = int(entry_quantidade.get())
    preco_produto = float(entry_preco.get())

    cursor.execute('''
            insert into produtos(nome,quantidade,preco)
            values (%s,%s,%s)''',
                    (nome_produto, quantidade_produto, preco_produto)
    )
    conn.commit()

def listar():
    listbox_estoque2.delete(0,tk.END)
    cursor.execute('select* from produtos')
    produtos = cursor.fetchall()
    for produto in produtos:
        listbox_estoque2.insert(tk.END,f"nome:{produto[0]},quantidade:{produto[1]},preco:{produto[2]}")

def excluir():
    nome_excluir = entry_excluir_nome.get()
    try:
        cursor.execute('select from produtos where nome = %s', (nome_excluir))
        produto = cursor.fetchone()
        if produto:
            cursor.execute('delete from produtos where nome = %s', (nome_excluir))
            conn.commit
            lable_excluir.config(text = "produto excluido")
        else:
            lable_excluir.config(text = "produto nao encontrado")
    except ValueError:
        lable_excluir.config(text = "produto invalido")

root = tk.Tk()
root.geometry ("500x400")
root.title("vendas")

lable_nome = tk.Label(root,text = "nome do produto:")
lable_nome.grid(row = 0, column = 0, padx = 10, pady = 5)
entry_nome = tk.Entry(root,width = 30)
entry_nome.grid(row = 0, column = 1, padx = 10, pady = 5)

lable_quantidade = tk.Label(root,text = "quantidade:")
lable_quantidade.grid(row = 1, column = 0, padx = 10, pady = 5)
entry_quantidade = tk.Entry(root,width = 30)
entry_quantidade.grid(row = 1, column = 1, padx = 10, pady = 5)

lable_preco = tk.Label(root,text = "preço:")
lable_preco.grid(row = 2, column = 0, padx = 10, pady = 5)
entry_preco = tk.Entry(root,width = 30)
entry_preco.grid(row = 2, column = 1, padx = 10, pady = 5)

button_cadastrar = tk.Button(root,text = "cadastrar", command = cadastrar)
button_cadastrar.grid(row = 3, padx = 2, pady = 10)

button_listar = tk.Button(root,text = "listar", command = listar)
button_listar.grid(row = 4, padx = 3, pady = 10)


listbox_estoque2 = tk.Listbox(root, height= 10, width = 40)
listbox_estoque2.grid()

lable_excluir = tk.Label(root,text = "informe o produto que deseja excluir")
lable_excluir.grid()
entry_excluir_nome = tk.Entry(root,width = 30)
entry_excluir_nome.grid()

button_excluir = tk.Button(root,text = "excluir", command = excluir)
button_excluir.grid(row = 35, padx = 4, pady = 10)

root.mainloop()
conn.close()