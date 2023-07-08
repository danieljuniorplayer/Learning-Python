cont=h=m=maior=teste=0
print('-' * 35)
while True:
    while True:
        idade=int(input('Qual a sua idade?: '))
        sexo=str(input('Qual seu sexo(M/F): ')).strip().upper()[0]
        if sexo not in 'MF':
            print(f'\033[31mSexo Inválido. Tente novamente\033[m')
        else:
            break
    cont += 1  # pessoas cadastradas
    if sexo in 'M':                     # homens cadastrados
        h+=1
    if sexo in 'F' and idade < 20:      # mulheres com menos de 20 anos
        m+=1
    if idade > 18:                      # pessoas maiores de 18
        maior+=1
    print('-' * 35)
    op=' '
    while op not in '01':
        op = str(input('[1] Cadastrar mais pessoas [0] Sair'))
    if op == '0':
        break
    print('-' * 35)
print('=' * 35)
print(f'homens cadastrados: {h}')
print(f'Pessoa maiores de 18 anos: {maior}')
print(f'Mulheres com menos de 20 anos: {m}')
print(f'Pessoas cadastradas: {cont}')
print('=' * 35)