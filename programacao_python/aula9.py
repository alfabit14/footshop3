videogames = []

def cadastrar():
    nome = input("digite o nome do jogo ")
    ano = int(input("digite o ano do jogo "))
    genero = input("digite o genero do jogo (ex: combate, estrategia... ")
    valor = input("digite o valor do jogo ")
    idade = input("digite a classificação de idade recomendada para o jogo ")
    maquina = input("digite os tipos de maquinas que rodarão o jogo ")
    jogo = {"nome":nome, "ano":ano, "genero":genero, "valor":valor, "idade":idade, "maquina": maquina }
    videogames.append (jogo)

def listar():
    for jogo in videogames:
        print (jogo)

def excluir():
    videogames_excluir = input("digite o nome do jogo a ser excluido ")
    for jogo in videogames:
        if (videogames_excluir==jogo["nome"]):
            videogames.remove(jogo)
            print ("jogo removido")

def buscar():
    jogo_buscado = input("digite o nome do jogo a ser pesquisado ")
    for jogo in videogames:
        if jogo["nome"] == jogo_buscado:
            return jogo
        else:
            return None


repetir = 1
while (repetir >= 1):
    resposta = int(input("digite 1 para cadastrar, 2 para listar, 3 para excluir e 4 para buscar "))
    if (resposta ==1):
        cadastrar()
    elif (resposta ==2):
        listar()
    elif (resposta ==3):
        excluir()
    elif (resposta ==4):
        print (buscar ())
    
    
    else:
        print ("opção invalida")
    repetir = int(input("digite 0 para parar de digitar "))
