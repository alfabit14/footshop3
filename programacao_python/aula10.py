estoqueprodutos = []

def cadastrarproduto():
    nomeproduto = input("digite o nome do produto ")
    quantidadeproduto = int(input("digite a quantidade do produto em estoque "))
    preçoproduto = float(input("digite o prço do produto "))
    produto = {"nome do produto":nomeproduto, "quantidade de produto":quantidadeproduto, "preço do produto":preçoproduto}
    estoqueprodutos.append(produto)
    print ("produto cadastrado")

def listar():
    for produto in estoqueprodutos:
        print (produto)

def buscarproduto(NomeProduto):
    for produto in estoqueprodutos:
        if produto ["nome do produto"] == NomeProduto:
            return produto
        return None



def vendas():
    NomeProduto = input("digite o produto a ser vendido ")
    produto = buscarproduto(NomeProduto)
    if produto is not None:
        quantidadedoestoque = produto["quantidade de produto"]
        quantidadevenda = int(input("digite a quantidade de produto a ser vendido "))
        if quantidadedoestoque >= quantidadevenda:
            produto["quantidade de produto"] = quantidadedoestoque - quantidadevenda
            print("venda realizada com sucesso")
        else:
            print ("venda não realizada")
    else:
        print ("produto não encontrado")

repetir = 1
while (repetir >= 1):
    resposta = int(input("digite 1 para cadastrar, 2 para listar e 3 para vender"))
    if (resposta ==1):
        cadastrarproduto()
    elif (resposta ==2):
        listar()
    elif (resposta ==3):
        vendas()
    else:
        print ("opção invalida")
    repetir = int(input("digite 0 para parar de digitar "))
