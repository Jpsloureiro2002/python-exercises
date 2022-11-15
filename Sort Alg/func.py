import random
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