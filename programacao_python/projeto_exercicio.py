import tkinter as tk

def enviar_mensagem():
    mensagem = entrada_mensagem.get()
    if mensagem:
        lista_mensagens.insert(tk.END, "Dimitri "+ mensagem)
        entrada_mensagem.delet(0,tk.END)

janela_chat = tk.Tk()
janela_chat.title("projeto")

lista_mensagens=tk.Listbox(janela_chat,width=50)
lista_mensagens.pack(padx=20,pady=20)
entrada_mensagem=tk.Entry(janela_chat,width=40)
entrada_mensagem.pack(padx=20,pady=20)
botao_enviar=tk.Button(janela_chat,text="enviar",command=enviar_mensagem )
botao_enviar.pack(padx=20,pady=20)

janela_chat.mainloop()