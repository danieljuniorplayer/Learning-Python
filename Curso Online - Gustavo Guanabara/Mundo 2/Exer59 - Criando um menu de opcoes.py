print('='*12,'As 4 operações','='*12)
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
op = True
while op:
      print('     Escolha uma das opções:\n'
            '     [1] Somar\n'
            '     [2] multiplicar\n'
            '     [3] Saber o maior valor\n'
            '     [4] Digitar novos números\n'
            '     [0] Sair do programa')
      op = int(input())
      if op == 0:
            op = False
      elif op == 1:
            print(f'    {n1} + {n2} = {n1+n2}')
      elif op == 2:
            print(f'    {n1} x {n2} = {n1 * n2}')
      elif op == 3:
            if n1>=n2:
                  print(f'    O maior valor é: {n1}')
            else:
                  print(f'    O maior valor é: {n2}')
      elif op == 4:
            print('=' * 40)
            n1 = int(input('Digite o primeiro valor: '))
            n2 = int(input('Digite o segundo valor: '))
      else:
            print('=' * 40)
            print('Escolha entre [0] e [4]')
      print('='*40)
print('------------- Fim Programa -------------')
print('='*40)