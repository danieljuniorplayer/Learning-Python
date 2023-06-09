#Exercicio pag 72(livro-introducao a programacao com python edicao 3)

#Exercício 3.7 --------------------------------------------------------
n1=int(input(' Digite o primeiro numero'))
n2=int(input(' Digite o Segundo numero'))
soma=n1+n2
print(f' A soma de {n1} mais {n2} é igual a {soma}\n')

#Exercicio 3.8---------------------------------------------------------
metro=float(input(' Digite os metros: '))
milimetro=metro*1000
print(f' {metro} metros é igual a {milimetro:.0f} milimetros\n')

#Exercicio 3.9 ------------------------------------------------------------
dia=int(input(' Digite quantidade de dias: '))
hora=int(input(' Digite quantidade de horas: '))
minuto=int(input(' Digite quantidade de minutos: '))
segundo=int(input(' Digite quantidade de segundos: '))
total=dia*86400+hora*3600+minuto*60+segundo
print(f'Esses valores transformados em segundos fica: {total} segundos\n')

#Exercício 3.10 Faça um programa que calcule o aumento de um salário. Ele deve
#solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento
#e do novo salário.
sal = float(input('Qual o seu salário?'))
porcentagem = int(input('Qual vai ser o aumento em porcentagem?'))
aumento = (sal*porcentagem)/100
novo = sal+aumento
print(f'Voce tera um aumento de {aumento:.2f} e seu novo salário vai ser de {novo:.2f} reais\n')

#Exercício 3.11 Faça um programa que solicite o preço de uma mercadoria e o percentual
#de desconto. Exiba o valor do desconto e o preço a pagar.
preco = float(input("Qual o preco da mercadoria?"))
percentual = int(input('Qual o desconto em porcentagem?'))
desconto = (preco * percentual)/100
pagar = preco - desconto
print(f'O valor do desconto fica: R${desconto:.2f}\nO preço a pagar fica: R${pagar:.2f}\n')

