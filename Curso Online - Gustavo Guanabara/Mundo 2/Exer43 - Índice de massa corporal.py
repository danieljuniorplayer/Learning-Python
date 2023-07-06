peso = float(input('Digite o seu peso? (Kg):'))
altura = float(input('Digite sua altura? (m):'))
imc = peso/altura**2
print(f'Seu IMC é de \033[34m{imc:.1f}\033[m')
if imc < 18.5:
    print('Você está \033[32mAbaixo\033[m do peso')
elif imc < 25:
    print('Você está com peso \033[32mIdeal\033[m')
elif imc < 30:
    print('Você está com \033[32mSobrepeso\033[m')
elif imc <= 40:
    print('Você está com \033[32mObsidade\033[m')
else:
    print('Atenção, você está com \033[32mObsidade Mórbida\033[m')