n1=int(input('Digite o primeiro valor:'))
n2=int(input('Digite o segundo valor'))

if n1==n2:
    print(f'\033[33mNão esiste\033[m valor maior,\n'
          f'todos são \033[34miguais\033[m')
elif n1>n2:
    print('O \033[33mprimeiro\033[m valor é o \033[34mmaior\033[m')
else:
    print('O \033[33msegundo\033[m valor é o \033[34mmaior\033[m')