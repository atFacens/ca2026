
numero = int(input('Digite um número inteiro: '))

resto = numero % 2 #  o resto da divisão

# if ternário
resposta = 'Este numero é par' if( resto == 0 ) else 'Este numero é impar'

print(resposta)