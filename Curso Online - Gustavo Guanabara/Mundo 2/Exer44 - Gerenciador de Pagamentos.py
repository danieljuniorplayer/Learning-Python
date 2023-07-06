
while True:
    preco = float(input('Qual o preço do produto? R$'))
    print('-'*43)
    print('[1] - Á vista no dinheiro ou cheque: 10% de desconto!\n'
          '[2] - Á vista no cartão: 5% de desconto!\n'
          '[3] - Em até 2x no cartão: preço normal!\n'
          '[4] - 3x ou mais no cartão: 20% de juros')
    condicao = int(input('Escolha de 1 a 4 uma das condição?'))
    print('-'*43)
    if condicao == 1:
        preco -= preco*0.10
    elif condicao == 2:
        preco -= preco*0.05
    elif condicao == 3:
        print(f'Você deverá pagar por mês R${preco / 2}')
    elif condicao == 4:
        preco += preco * 0.20
        parcelas = int(input('Quantas parcecelas?'))
        print(f'Você deverá pagar por mês R${preco/parcelas}')
    else:
        condicao = 0
        print('Opção invalida, você deveria escolher entre 1 e 4!')
    if condicao !=0:
        print(f'Você deverá pagar no total R${preco}')
    print('-' * 43)
    op = int(input('Digite [1] para tentar novamente ou [0] para sair do programa'))
    if op == 0:
        break
print('-'*15,'FIM SISTEMA','-'*15)