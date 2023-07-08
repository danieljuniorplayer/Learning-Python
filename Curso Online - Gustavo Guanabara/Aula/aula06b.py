cont = str(input('Digite algo'))
print(cont)
print(type(cont))  # mostra qual tipo primitivo pertence
print(cont.isnumeric())  # mostra se o valor pode ser transformado em numero
print(cont.isalpha())   #mostra se o valor he uma letra
print(cont.isalnum())   #mostra se e alfanumerico, ou seja letra e/ou numero
print(cont.isupper())   #verifica se estar somente com letras maiusculas

if cont.isalpha():
    print('O voce digitou uma letra')
elif cont.isalpha()==False:
    print('voce nao digitou uma letra')
else:
    print('\nagora bora ver se e um numero\n')

if cont.isnumeric()==True:
    print('o valor digitado  eh um numero')
elif cont.isnumeric()==False:
    print('O valor digitado nao eh numero')
else:
    print('fim sistema')
