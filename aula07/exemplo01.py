# Faça a soma um conjunto de 5 números inteiros digitados pelo usuário

cont = 1
soma = 0

while( cont <= 5 ):
    numero = int(input('Digite um número inteiro: '))
    soma += numero
    cont += 1

print('soma =', soma)
