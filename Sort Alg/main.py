import os
from func import *
def cls_():
    os.system('cls')

def vprint(vetor,n):
    for i in range(n):
        print(vetor[i],end=" ")
vetor=[]
cls_()
l = int(input("Insira quantos Numeros Criar:\n"))
cls_()
for i in range(l):
    vetor.append(i+1)
leng = len(vetor)
shuffle.shuffle(vetor,leng)
vprint(vetor,leng)
print("\n")
sort.SortRec(vetor, leng)
vprint(vetor,leng)