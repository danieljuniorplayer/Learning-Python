n1 = float(input('Digite um valor em metros: '))
km = n1/1000
hm = n1/100
dam = n1/10
dm = n1*10
cm = n1*100
mm = n1*1000
print(f'Esse valor corresponde:\n'
      f'km: {km}\n'
      f'hm: {hm}\n'
      f'dam: {dam}\n'
      f'dm: {dm:.0f}\n'
      f'cm: {cm:.0f}\n'
      f'mm: {mm:.0f}\n')