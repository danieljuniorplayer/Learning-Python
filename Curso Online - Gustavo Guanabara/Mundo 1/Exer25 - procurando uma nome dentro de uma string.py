nome = str(input('Digite seu nome:')).strip().lower()
find = str(input('Digite o nome que você quer verificar: ')).strip().lower()
#resposta = nome.find(find+' ') != -1
resposta = find+' ' in nome

print(nome.find(find))
print('No seu nome, tem a palavra "SILVA"? :',resposta)