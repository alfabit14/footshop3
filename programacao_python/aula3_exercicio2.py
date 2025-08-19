p = int(input('digite seu peso '))
a = float(input('digite sua altura '))

imc = (p / (a * a))

if (imc <= 18):
    print("baixo peso")
elif (imc > 18 and imc <= 25):
    print('peso normal')
else:
    print ('obesidade')
