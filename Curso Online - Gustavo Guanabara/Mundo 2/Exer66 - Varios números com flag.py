cont=soma=0
while True:
    n = int(input('Digite um número: [999 Parar]'))
    if n == 999:
        break
    cont+=1
    soma+=n
print(f'No total{cont:^20} números digitados') # centralisado com 5 caracteres
print(f'A soma desses número: {soma:-^20}')     # centralizado com caracteres
media = soma/cont
print(f'A média é {media:->20.2f}')     # alinhado a direita com 20 "-" e 2 pontos flutuantes