
semana = 6

if( semana == 1 ):
    print('segunda')
elif( semana == 2 ):
    print('terça')
elif( semana == 3 ):
    print('quarta')
elif( semana == 4 ):
    print('quinta')
elif( semana == 5 ):
    print('sexta')
elif( semana == 6 or semana == 7 ):
    print('descanso')
else:
    print('Valor inválido')


match semana:
    case 1:
        print('segunda')
    case 2:
        print('terça')
    case 3:
        print('quarta')
    case 4:
        print('quinta')
    case 5:
        print('sexta')
    case 6 | 7:
        print('descanso')
    case _:
        print('Valor inválido')
        