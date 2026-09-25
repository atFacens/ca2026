# Escreva um programa que leia 2 números e um sinal de uma operação matemática
# e informe o resultado desta operação
# 34 - 4 = 30 
# ==> 34 ==> 4 ==> - ==> 30

# entrada de dados
numero1 = float(input('Digite o primeiro valor: '))
numero2 = float(input('Digite o segundo valor: '))
operador = input('Qual a operação? ( + - * / ): ')

# processamento
# if(operador == '+'):

match operador:
    case '+': resultado = 'Resposta = ' + str(numero1 + numero2)
    case '-': resultado = 'Resposta = ' + str(numero1 - numero2)
    case '*': resultado = 'Resposta = ' + str(numero1 * numero2)
    case '/': 
        if(numero2 == 0):
            resultado = 'Divisão por zero!'
        else:
            resultado = 'Resposta = ' + str(numero1 / numero2)
    case _: resultado = 'Operação inválida'


# exibir os resultados
print(resultado)