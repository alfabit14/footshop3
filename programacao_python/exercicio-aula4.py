i = 0
while (i<3):
    print ("digite 1 para matematica\n",
    "digite 2 para porugues\n",
    "digite 3 para ingles"   )
    materias = int(input("digite o numero de sua materia "))

    if (materias == 1):
        print ("matematica")
    elif (materias == 2):
        print ("portugues")
    else:
        print ("ingles")
    i = i + 1
print ('FIM')