n1 = float(input('Qual é o preço do produto R$'))
desconto = n1 - (n1*0.05)
print(f'O produto que custava R$\033[32m{n1:.2f}\033[m, na promoção de \033[33m5%\033[m, vai custa R$\033[32m{desconto:.2f}\033[m')
