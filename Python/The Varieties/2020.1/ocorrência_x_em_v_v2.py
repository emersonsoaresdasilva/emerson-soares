'''
Crie uma função que receba como parâmetros um valor inteiro X, um vetor de
inteiros V e o tamanho de N de V.
A função deverá retornar o índice da primeira ocorrência de X em V, ou -1
caso X não esteja em V.

Restrições; Funções/métodos built-in
Permitidos: range()
'''
#-----------------------------------
#               FUNÇÃO
#-----------------------------------
def indice(x, vetor, tamanho):
    for i in range(tamanho): #[0..n[
        if vetor[i]==x: return i
    return -1

#-----------------------------------
#        PROGRAMA PRINCIPAL
#-----------------------------------
tamanho = int(input('Tamanho do vetor: '))
vetor = tamanho * [0]

for i in range(tamanho):
    vetor[i] = int(input('Valor: '))

x = int(input('Valor procurado: '))
ind = indice(x,vetor,tamanho)

if ind != -1:
    print('Item encontrado! Índice:',ind)
else:
    print('Item não encontrado!')



    
