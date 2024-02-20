#
# #COLECOES
# # TUPLAS
# #UMA COLEÇAO IMUTAVELLLL
# nomes = ("Goku", "Vegeta", "Trunks", "Gohan") #tuplas, divididas por parenteses
#
#
# #SLICING
#
# print(nomes[0])
# print(nomes[:2]) #pegar todos os elementos até o numero 2, EXCLUSIVE
# print(nomes[1:3]) #pegar o primeiro argumento inclusive
# print(nomes[-2])
#
# #upgrade
# nomes[0] = "Bulma"
#
# #LISTAS
# nomes = ["Goku", "Vegeta", "Trunks", "Gohan"] #lista, divididas por colchetes
# # ADD
# nomes.append('Bulma')
# # UPDATE
# nomes[0] = 'Goten'
# # DELETE
# #sem indice
# nomes.remove('Trunks')
# del nomes[2] #remoçao por indice
# #SELECT
# print(nomes)


# #CONJUNTOS
# # nao guarda a ordem dos elementos
# #permite inserçao
# nomes = {"Goku", "Vegeta", "Trunks", "Gohan"}
# nomes.add('Bulma')
# nomes.add('Goku')
# print(nomes)
#
# #REMOVE
# nomes.remove('Gohan')
# print(nomes)
#
# #UPDATE (NAO FUNCIONA)
#


# #DICIONARIOS
# #INDICES CUSTOMIZAVEIS
#
# pessoa = {'nome': 'Goku', 'idade': 42}
#
# #ADD
# pessoa['sexo'] = 'M' #adicionando novo chave valor
#
# #UPDATE
# pessoa['nome'] = 'Goten'
#
# #DELETE
# del pessoa['idade']
#
# #SELECT
# print(pessoa)


#COLECOES ALINHADAS

pessoa = {'nome': 'Goku', 'idade': 42}
pessoa2 = {'nome': 'u', 'idade': 12}

nomes = [pessoa, pessoa2]
print(nomes[1]['nome']) #pegando o nome da pessoa 2
