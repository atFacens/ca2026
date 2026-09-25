# leia um conjunto de 5 valores e some os positivos


# Solução 1

# cont = 1
# soma = 0

# while( cont <= 5 ):
#     numero = int(input('Digite um número inteiro positivo: '))
#     if(numero <= 0):
#         print('Valor incorreto!')
#     else:
#         soma += numero
#     cont += 1

# print('soma =', soma)


# solução 2

cont = 1
soma = 0

while( cont <= 5 ):
    numero = int(input('Digite um número inteiro positivo: '))
    cont += 1
    if(numero <= 0):
        print('Valor incorreto!')
        continue
    soma += numero
    
print('soma =', soma)