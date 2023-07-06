
lista = []  # declaração do vetor com a classse list
#print(dir(lista))   # verifica todos os métodos do vetor
#print(type(lista))  # verifica o tipo de vareável
soma=0
cont=0
for c in range(0,6):
    n = int(input(f'Digite o {c+1}° número'))
    if n%2 == 0:
        soma += n
        cont+=1
        lista.append(n)     # salva os valores de "n" na lista  incrementando


print('Quantidade de números pares: ',cont)
print('Lista dos números pares: ',lista)
print('Soma dos números pares: ',soma)