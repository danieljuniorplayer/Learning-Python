n1 = float(input('Digite um valor em metros: '))
km = n1/1000
hm = n1/100
dam = n1/10
dm = n1*10
cm = n1*100
mm = n1*1000
A = '\033[7:34m'
F = '\033[m'
print(f'Esse valor corresponde:\n'
      f' {A}{km:9.2f}{F} km\n'
      f' {A}{hm:9.2f}{F} hm\n'
      f' {A}{dam:9.2f}{F}dam\n'
      f' {A}{dm:9.2f}{F} dm\n'
      f' {A}{cm:9.2f}{F} cm\n'
      f' {A}{mm:9.2f}{F} mm\n')