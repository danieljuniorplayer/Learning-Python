#Transforma horas para minutos,
# se for mais de 1 hora, continua igual
# se for menos, transforma em minutos
hora = float(input('Digite a quantidade em horas'))
if hora < 1:
    minuto = hora*60
    print(f'Esse tempo equivale a {minuto:.0f} minutos')
else:
    print(hora)