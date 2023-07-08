numero =1
lista= []
qtd =soma =0
while numero !=0:
    print('=' * 65)
    while numero !=0:
        numero=int(input('Digite um número inteiro para somar: | [0] Ver Resultados: '))
        if numero!=0:                   # soma e quantidade
            lista.append(numero)
            soma += numero
            qtd += 1
    print('='*65)
    print(f'A média desses valores é igual a: {soma/qtd:.2f}')
    print(f'O maior valor digitado: {max(lista)}')
    print(f'O menor valor digitado: {min(lista)}')
    print('=' * 65)
    numero = int(input('\033[31m[1] Adicionar mais números: | [0] Sair do Programa\033[m'))