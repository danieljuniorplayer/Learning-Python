import datetime
from datetime import date
ano_nascimento = int(input('Digite apenas seu ano de nascimento:'))
ano_atual = date.today().year
idade_anos = ano_atual - ano_nascimento

print(f'Nesse ano você faz {idade_anos} anos de idade')
if idade_anos <= 9:
    print(f'Sua categoria é Mirim')
elif idade_anos <= 14:
    print(f'Sua categoria é Infantil')
elif idade_anos <= 19:
    print(f'Sua categoria é Junior')
elif idade_anos <= 20:
    print(f'Sua categoria é Sénior')
else:
    print(f'Sua categoria é Master')
