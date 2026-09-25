# Faça a soma um conjunto de X números inteiros digitados pelo usuário
# Pergunte para o usuário quantos números ele quer digitar

cont = 1
soma = 0

quantidade = int(input('Quantos números você quer digitar?  '))

while( cont <= quantidade ):
    numero = int(input('Digite um número inteiro: '))
    soma += numero
    cont += 1

print('soma =', soma)
