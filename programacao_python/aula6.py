def caucular_media(ac1, ac2):
    total = (ac1 + ac2) / 2
    return (total)

login = input("digite o login ")
if (login == "Dimitri" or login == "dimitri"):
    senha = int(input("digite a senha "))
    if (senha == 123):
        print ("entrando no sistema")
        quantidade = int(input("digite a quantidade de alunos"))
        for i in range(0, quantidade):
            nome = input("informe o nome do aluno")
            ac1 = float(input("informe aprimeira nota"))
            ac2 = float(input("informe a segunda nota"))
            print  (caucular_media(ac1, ac2))
    else:
        print ("senha invalida")
else:
    print ("login invalido")