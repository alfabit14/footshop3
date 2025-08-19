lista_alunos = []

def cadastrar ():
    nome = input("digite o nome do aluno ")
    idade = input("digite a idade do aluno ")
    aluno = {"nome":nome, "idade":idade}
    lista_alunos.append (aluno)

def listar ():
    for aluno in lista_alunos:
        print(aluno)

def excluir ():
    aluno_excluir = input("digite o nome para ser excluido ")
    for aluno in lista_alunos:
        if (aluno_excluir ==aluno["nome"]):
            lista_alunos.remove (aluno)
            print ("aluno removido")

def buscar_aluno (nome_buscado):
    for aluno in lista_alunos:
        if aluno["nome"] == nome_buscado:
            return aluno
        else:
            return None

def atualizar_aluno():
    nome_antigo = input("Digite o nome a ser atualizado: ")
    aluno = buscar_aluno(nome_antigo)
    if aluno is not None:
        novo_nome = input("Digite o novo nome: ")
        aluno["nome"] = novo_nome
        print("Nome atualizado com sucesso!")
    else:
        print("Aluno não encontrado.")

repetir = 1
while (repetir >=1):
    resposta = int(input("digite 1 para cadastrar, 2 para listar, 3 para excluir, 4 para buscar e 5 para atualizar "))
    if (resposta ==1):
        cadastrar()
    elif (resposta ==2):
        listar()
    elif (resposta ==3):
        excluir()
    elif (resposta ==4):
        nome_buscado = input("digite o nome para ser pesquisado ")
        print (buscar_aluno(nome_buscado))
    elif (resposta ==5):
        atualizar_aluno()
    else:
        print("opção invalida")
    repetir = int(input("digite 0 para parar de digitar "))
