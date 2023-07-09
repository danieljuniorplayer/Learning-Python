extenso =('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez',
          'onze','doze','treze','quartoze','quize','dezesseis','dezessete','dezoito','dezenove','vinte')




numero =int(input('Digite um número: '))
while numero >20 or numero<0:
    print('Tente novamente: ')
    numero = int(input('Digite um número: '))
print(extenso[numero])

numero =int(input('Digite um número: '))
while not numero in range(0,len(extenso)):
    print('Tente novamente: ')
    numero = int(input('Digite um número: '))
print(extenso[numero])

while True:
    numero =int(input('Digite um número: '))
    if 20>=numero>=0:
        break
    print('Tente novamente...')
print(extenso[numero])

op = True
while op:
    numero = int(input('Digite um número: '))
    if 20 >= numero >=0:
        print(extenso[numero])
        op=False
    else:
        print('Tente Novamente:')
