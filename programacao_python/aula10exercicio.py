estoque_de_produtos = []

def cadastrar():
    nome_produto = input("digite o nome do produto ")
    quantidade_prouto = int(input("digite a quantidade do produto "))
    preço_produto = input("digite o preço do produto ")
    produto = {"nome":nome_produto,"quantidade":quantidade_prouto,"preço":preço_produto }
    estoque_de_produtos.append(produto)

def listar():
    for produto in estoque_de_produtos:
        print (produto)

def buscar_produto(nome_buscado):
    for produto in estoque_de_produtos:
        if produto["nome"] == nome_buscado:
            print(produto)
            return produto  # Retorna o produto encontrado
    print("Produto não encontrado")
    return None  # Retorna None caso o produto não seja encontrado

def vender_produto():
    nome_buscado = input("digite o nome do produto a ser buscado ")
    produto = buscar_produto(nome_buscado)
    if produto is not None:
        produto_atual = produto["quantidade"]
        quantidade_venda = int(input("digite a quantidade de produto a ser vendido "))
        if produto_atual >= quantidade_venda:
            produto["quantidade"] = produto_atual - quantidade_venda
            print ("venda concluida")
        else:
            print("quantidade de produto insuficiente")
    else:
        print ("produto inexistente")


repetir =1
while (repetir >= 1):
    resposta = int(input("digite 1 para cadastrar, 2 para listar, 3 para buscar e 4 para vender "))
    if (resposta == 1):
        cadastrar()
    elif (resposta == 2):
        listar()
    elif (resposta == 3):
        nome_buscado = input("digite o nome a ser buscado ")
        buscar_produto(nome_buscado)
    elif (resposta == 4):
        vender_produto()
    else:
        print ("opção invalida")
    repetir = int(input("digite 0 para parar de digitar "))