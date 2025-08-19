numeros = [9, 8, 0, 5.5, 9, 6]
for i in numeros:
    if i == 9 :
        numeros.remove (i)
print (numeros)









medias = [9, 2, 6.9, 8, 1, 7, 10, 9, 9.9, 6]
print (medias)
for i in  medias:
    if i <= 6.9:
        medias.remove(i)
print (medias)









lista_nomes = []
quantidade = int(input('digite a quantidade de nomes'))
for i in range (0, quantidade):
    nome = input("digite seu nome ")
    lista_nomes.append (nome)
print (lista_nomes)





listanumeros = []
resposta = int(input("digite 1 para cadastrar um numero"))
while(resposta == 1):
    num = int(input("digite um numero"))
    listanumeros.append (num)
    resposta = int(input("digite 1 para cadastrar um numero"))
print (listanumeros)