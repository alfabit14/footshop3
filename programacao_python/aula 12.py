import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "aulamedia"
)
cursor = conn.cursor()


n1 = float(input("digite a primeira nota "))
n2 = float(input("digite a segunda nota "))
media = (n1 + n2)/2
print (media)

insert_query = ''' 
    insert into aluno(n1,n2,media)
    values(%s,%s,%s)
'''
insert_values = (n1,n2,media)

cursor.execute(insert_query, insert_values)
conn.commit()

conn.close()