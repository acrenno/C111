import numpy as np

# NUMEROS ALEATORIOS
# random

#seed = semente / semente aleatoria

np.random.seed(10)

arr = np.random.randint(1, 11, 15) #gerar numeros de 1 a 10, 15 numeros
#print(arr) #gera numeros aleatorios independentes da maquinaz

#extraindo elementos unicos e retornar com o numero de repetiçoes de cada numero
# primeiro  numpyarray sai quais sao os elementos unicos, e o segundo, quantas vezes se repete
#print(np.unique(arr, return_counts = True))


#OPERALOES EM MATRIZES

mtz = arr.reshape(3,5)
##print(mtz)
#saindo com a soma da primeira linha do array
#axis = 1, soma da horizontal/ 0 para soma vertical
#print(mtz.sum(axis=1)[0])
#soma vertical
##print(mtz.sum(axis=0)[0])


#BROADCASTING
#print(0.5*mtz)

#CONDICIONAIS
print(mtz)
#extrair numeros pares da matriz
cond = mtz%2==0
#print(mtz[cond])

#sai com os numeros que sao maiores que a media da soma dos elementos da matriz
maiormedia = mtz>mtz.mean()
#print(mtz[maiormedia])

#ANALISE TEXTUAL
arr = np.array(['Pedro', 'Arthur', 'Anna', 'Maciel'])
#retorna a posição que se encontra a letra a
result = np.char.find(arr, 'a')
cond3 = np.char.find(arr, 'a')>=0
print(arr[cond3])



