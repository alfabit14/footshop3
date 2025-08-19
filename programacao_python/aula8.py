lista_alunos = []

def cadastrar ():
    nome = input("digite o nome do aluno ")
    ano = input("digite o ano do aluno ")
    idade = int(input ("digite a idade "))
    aluno = {"nome":nome,"ano":ano, "idade":idade}
    lista_alunos.append (aluno)

def listar ():
    for aluno in lista_alunos:
        print (aluno)

def excluir ():
    nome_excluir =input ("digite o nome que quer excluir")
    for aluno in lista_alunos:
        if (nome_excluir == aluno["nome"]):
            lista_alunos.remove(aluno)
            print ("aluno removido")

def buscar_aluno (nome_buscado):
    for aluno in lista_alunos:
      if aluno["nome"]  == nome_buscado:
          return aluno
      else:
          None
    
def atualizar_aluno ():
    nome_antigo = input("digite o nome para ser atualizado ")
    aluno = buscar_aluno(nome_antigo)
    if aluno is not None:
        novo_nome = input ("digite o novo nome ")
        aluno ["nome"] = novo_nome
        print("aluno atualizado")
    else:
        print ("aluno nao encontrado")

repetir = 0
while (repetir ==0):
    resposta = int(input("digite 1 para cadastrar, digite 2 para listar, 3 para excluir, 4 para buscar e 5 para modificar "))
    if (resposta ==1):
        cadastrar()
    elif(resposta ==2):
        listar()
    elif(resposta ==3):
        excluir()
    elif(resposta ==4):
        nome_buscado = input("digite o nome do aluno a ser buscado ")
        print (buscar_aluno(nome_buscado))
    elif(resposta ==5):
        atualizar_aluno()
    else:
        print ("resposta invalida")
    repetir = int(input("se quiser repetir digite 0 "))