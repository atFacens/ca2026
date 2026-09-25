# some um conjunto de 5 valores positivos

cont = 1
soma = 0

while( cont <= 5 ):
    numero = int(input('Digite um número inteiro positivo: '))
    if(numero <= 0):
        print('Valor incorreto!')
        continue

    soma += numero
    cont += 1

print('soma =', soma)