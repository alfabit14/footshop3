import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "nomeeidade"
)
cursor = conn.cursor()


nome = input("diga o seu nome ")
idade = int(input("diga a sua idade "))
print (nome, idade)

insert_query = '''
    insert into pessoa(nome, idade)
    values(%s,%s)
'''

insert_values = (nome, idade)

cursor.execute (insert_query, insert_values)
conn.commit()

conn.close()