import mysql.connector

 

# Conectando ao banco de dados

conn = mysql.connector.connect(

    host="localhost",

    user="root",

    password="root",

    database="estoque "

)

cursor = conn.cursor()

 

def cadastrar():

    nome_produto = input("Digite o nome do produto: ")

    quantidade_produto = int(input("Digite a quantidade do produto: "))

    preco_produto = float(input("Digite o preço do produto: "))

   

    # Inserir os dados do produto no banco de dados

    insert_query = '''

        INSERT INTO produtos (nome, quantidade, preco)

        VALUES (%s, %s, %s)

    '''

    insert_values = (nome_produto, quantidade_produto, preco_produto)

   

    cursor.execute(insert_query, insert_values)

    conn.commit()

    print("Produto cadastrado com sucesso!")

 

def listar():

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

 

repetir = True

while repetir:

    resposta = int(input("Digite 1 para cadastrar, 2 para listar, 3 para buscar e 4 para vender: "))

   

    if resposta == 1:

        cadastrar()

    elif resposta == 2:

        listar()

    elif resposta == 3:

        nome_buscado = input("Digite o nome a ser buscado: ")

        buscar_produto(nome_buscado)

    else:

        print("Opção inválida")

   

    repetir = int(input("Digite 0 para parar de digitar: ")) != 0

 

conn.close()