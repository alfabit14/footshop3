def somar (n1, n2):
    total_soma = (n1 + n2)
    return (total_soma)

def subtrair (n1, n2):
    total_subtracao = (n1 - n2)
    return (total_subtracao)

def multiplicacao (n1, n2):
    total_multiplicacao = (n1 * n2)
    return (total_multiplicacao)

def divisao (n1, n2):
    total_divisao = (n1 / n2)
    return (total_divisao)

n1 = int(input("digite o primeiro numero"))
n2 = int(input("digite o segundo numero"))
print (somar (n1, n2))
print (subtrair(n1, n2))
print (multiplicacao(n1, n2))
print (divisao (n1, n2))