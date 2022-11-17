import os
from func import *
clsp = lambda: os.system('cls') 
vetor=[]
Prompt.Menu()
clsp()
cont = 1
while cont == 1:
    maximo = int(input("Primeiro insere maior valor a ser gerado:\n"))
    clsp()
    while maximo <= 1:
        clsp()
        maximo = int(input("Vala escreve um número maior que 2 -.-:\n"))
    clsp()
    minimo = int(input("Agora um valor minimo esse sim pode ser 0:\n"))
    while (minimo > maximo):
        clsp()
        minimo = int(input(f"De preferencia um valor menor que o maximo ({maximo}) ne .-.:\n"))
    clsp()
    l = int(input(f"Agora insere o comprimento do vetor, maior que 0 e convem não ser maior que o maximo ({maximo}) tambem:\n"))
    while l >= maximo:
        clsp()
        l = int(input(f"E que tal um valor menoor que o maximo que é ({maximo}):\n"))
    while l <= 1:
        clsp()
        l = int(input(f"Olha quem me dera mas um vetor com comprimento negativo ou pequeno é foda:\n"))
    clsp()
    print(f"Tamanho do Vetor:{l}        Min:{minimo}          Max:{maximo}")
    print("\nVetor:")
    Rand.Vrand(vetor,l,minimo,maximo)
    leng = len(vetor)
    shuffle.shuffle(vetor,leng)
    Prompt.vprint(vetor,leng)
    print("\n\nVetor Final:")
    sort.SortRec(vetor, leng)
    Prompt.vprint(vetor,leng)
    x = input("\nContinuar?")
    if x == "y":
        cont = 1
    elif x == "Y":
        cont = 1
    elif x == "n":
        cont = 0
    else:
        cont = 0
    clsp()