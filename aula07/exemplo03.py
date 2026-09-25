# Faça a soma um conjunto de números inteiros digitados pelo usuário
# Pergunte para o usuário quantos números ele quer digitar, mas no máximo aceite 10 valores

cont = 1
soma = 0

quantidade = int(input('Quantos números você quer digitar?  '))

if(quantidade > 10):
    print('Isso é muito! Vamos até 10')
    quantidade = 10

while( cont <= quantidade ):
    numero = int(input('Digite um número inteiro: '))
    soma += numero
    cont += 1

print('soma =', soma)
