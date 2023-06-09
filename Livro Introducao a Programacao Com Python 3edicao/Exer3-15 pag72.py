"""Exercício 3.15 Escreva um programa para calcular a redução do tempo de vida de
um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos
ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro,
e calcule quantos dias de vida um fumante perderá. Exiba o total em dias."""

cigarro_dia = int(input('Quantos cigarros voce fuma por dia? '))
anos = int(input('A quantos anos voce fuma? '))

total_cigarro = (anos * 365) * cigarro_dia  # total de cigarros fumados durante esse periodo
minuto_perdido = total_cigarro * 10         # total de minutos perdidos durante esse periodo
dia_perdido = minuto_perdido/(60*24)        # transformando minutos em dias

print(f'Se voce fumou {cigarro_dia} cigarros por dia, '
      f'durante {anos} anos, voce perdeu {dia_perdido:.0f} dias da sua vida')
