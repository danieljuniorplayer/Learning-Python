numero =qtd =soma =0
while numero !=999:
    numero=int(input('Digite um número inteiro: |[999 Sair]'))
    if numero!=999:
        soma+=numero
        qtd+=1
print('A quantidade de números digitados foi: ',qtd)
print(f'A soma desses números é igual a: {soma:20}')