

valor = float(input('Digite o valor'))
apagar = valor
atual = 50
i=0
while True:
    if atual <= apagar:          # 88 >= 50, 38>= 20, 18>=10, 8>=5, 3>=1,2>=1, 1>=1
        apagar = apagar - atual  # 88 = 88 - 50 (valor =38, 18,8,3,2,1)
        i+=1 #1,1,1
    else:
        print(f'{i} notas de {atual}')  # 1:50, 1:20, 1:10, 1:5
        if apagar == 0:
            break

        if atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        while True:
            if apagar < 0:
                apagar = apagar - atual
                i+=1
            else:
                print(f'{i} notas de {atual}')  # 1:50, 1:20, 1:10, 1:5
                if apagar == 0:
                    break
                if atual == 0.50:
                    atual = 0.10
                elif atual == 0.10:
                    atual = 0.05
                elif atual == 0.05:
                    atual = 0.02
                elif atual == 0.02:
                    atual = 0.01
                i = 0
        i=0