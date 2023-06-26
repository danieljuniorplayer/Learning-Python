
valor=input('Digite algo\n')
F = '\033[0:31mFalse\033[m'
T = '\033[0:34mTrue\033[m'

print('O tipo primitivo desse valor eh',type(valor))
print(f'So tem espacos?',T if valor.isspace() == True else F)
print('E apenas numero?',T if valor.isnumeric() ==True else F)
print('E apenas alfabetico?',T if valor.isalpha()==True else F)
print('E alfanumerico?',T if valor.isalnum()==True else F)
print('E Totalmente maiusculo?',T if valor.isupper()==True else F)
print('E Totalmente minusculo?',T if valor.islower()==True else F)
print('Esta capitalizado',T if valor.istitle()==True else F)

