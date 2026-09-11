# operadores lógicos
# E(and) OU(or) NAO(not)

esta_sol = False
eh_feriado = False

vou_para_praia = esta_sol and eh_feriado # as duas partes tem que ser True para ter resultado Treu
print('Vou para a praia?', vou_para_praia)

tem_lampada_igual = False
tem_uma_lapada_similar = False

pode_trocar_lampada = tem_lampada_igual or tem_uma_lapada_similar # True se PELO MENOS UMA for True
print('Pode trocar? ', pode_trocar_lampada)

print('Não pode trocar', not pode_trocar_lampada)