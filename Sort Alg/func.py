import random
import os
def cls_():
    os.system('cls') 

class Prompt:
 
    def vprint(vetor,n):
        for i in range(n):
            print(vetor[i],end=" ")
    def Menu():
        cls_()
        x = input("Ola bem vindo aos meus Exercicos :3\nPor agora não ha muito a fazer mas podereas ver comoalguns dos meus algoritmos funcionam\nClica no Enter ou em qualquer letra para comessar :3")
class sort:
    def SortRec(vetor, leng):
        if leng <= 1:
            return
        
        sort.SortRec(vetor,leng -1)
        last = vetor[leng-1]
        j = leng-2
        while (j >=0 and vetor[j]>last):
            vetor[j+1] = vetor[j]
            j = j-1

        vetor[j+1] = last
class shuffle:
    def shuffle(v, l):
        f = 0
        while (f <= l-1):
            index = random.randrange(0, l-1)
            temp = v[f]
            v[f] = v[index]
            v[index] = temp
            f +=1
        return

class Rand():
    def Vrand(new_vet,l,min,max):
        if min > max:
            return print("Imposivel realizar o pedido 1")
        if min < 0:
            return print("Imposivel realizar o pedido 2")
        if max < l:
            return print("Imposivel realizar o pedido 3")
        i=0
        while i < l:
            check = 0
            v = random.randrange(min,max)
            if i > 0:
                for h in new_vet:
                    if v == h:
                        check = 1
                        break
                if check == 0:
                    new_vet.append(v)
                    i = i+1
            else:
                new_vet.append(v)
                i = i+1

        