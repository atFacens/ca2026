
numero = int(input('Digite um número inteiro: '))

resto = numero % 2 #  o resto da divisão

if( resto == 0 ):
    resposta = 'Este numero é par'
else:
    resposta = 'Este numero é impar'

print(resposta)