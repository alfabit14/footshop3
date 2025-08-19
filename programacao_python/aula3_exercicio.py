n = int(input('digite o primeiro numero numero '))
n2 = int(input('digite o segundo numero '))
n3 = int(input('digite o terceiro numero '))

r = (n + n2 + n3)

print ("o resultado da equação foi",r)

if (r < 10):
    print ("o resultado foi menor 10")
elif (r == 10):
    print ('o resultado foi 10')
else:
    print ('o resultado foi maior que 10')
