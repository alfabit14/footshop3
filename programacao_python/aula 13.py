import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "estoque"
)
cursor = conn.cursor()


lista_estoque = []


def cadastro_de_produto():
    nome = input("digite o nome do seu produto ")
    quantidade = int(input("digite a quantidade de produtos "))
    preco = input("digite o preço do produto")
    produto = {"nome":nome,"quantidade":quantidade,"preço":preco}
    lista_estoque.append (produto)

    insert_quarry = '''insert into produtos(nome, quantidade, preco)values (%s, %s, %s)'''
    insert_values = (nome,quantidade,preco)
    cursor.execute(insert_quarry, insert_values)
    conn.commit()


def listar_produto():
    # Recuperar todos os produtos da tabela
    select_query = '''
        SELECT * FROM produtos
    '''
    cursor.execute(select_query)
    produtos = cursor.fetchall()
    for produto in produtos:
        print(produto)

def buscar_produto(nome_buscado):
    # Buscar o produto no banco de dados
    select_query = '''
        SELECT * FROM produtos WHERE nome = %s
    '''
    cursor.execute(select_query, (nome_buscado,))
    produto = cursor.fetchone()
    if produto is not None:
        print(produto)
        return produto
    else:
        print("Produto não encontrado")
        return None

def vendas():
    nome_buscado = input("digite o produto que você que comprar")
    produto = buscar_produto(nome_buscado)
    if produto is not None:
        produto_atual = produto[1]
        quantidade = int(input("digite aquantidade que você quer comprar"))
        if produto_atual >= quantidade:
            estoque = produto_atual - quantidade
            update_quary = '''update produtos set quantidade = %s where nome = %s'''
            cursor.execute(update_quary, (estoque,nome_buscado))
            conn.commit()
      
        else:
            print("quantidade insuficiente")


    else:
        print("produto inexistente")


repetir = 1
while repetir >= 1:

    resposta = int(input("digite 1 para cadastrar, 2 para listar, 3 para buscar e 4 para vender"))
    if resposta == 1:
        cadastro_de_produto()
    elif resposta ==2:
        listar_produto()
    elif resposta == 3:        
        nome_buscado = input("digite o nome do produto a ser buscado")
        buscar_produto(nome_buscado)
    elif resposta == 4:
        vendas()
    else:
        print("opção invalida")

    repetir = int(input("digite 0 para parar"))

