print('=-'*20)
print('Analizador de triângulo')
print('=-'*20)
reta1 = float(input('Digite o comprimento da primera reta:'))
reta2 = float(input('Digite o comprimento da segunda reta:'))
reta3 = float(input('Digite o comprimento da terceira reta:'))

if reta1+reta2>reta3 and reta2+reta3>reta1 and reta3+reta1>reta2:
    print(f'Os segmentos acima PODEM FORMAR um triagulo!✔')
else:
    print(f'Os segmentos acima NÃO PODEM FORMAR um triagulo!❌')







'''reta =[reta1,reta2,reta3]
reta.sort()
if reta[0] + reta[1] > reta[2]:
    print(f'Os segmentos acima PODEM FORMAR um triagulo!✔')
else:
    print(f'Os segmentos acima NÃO PODEM FORMAR um triagulo!❌')'''