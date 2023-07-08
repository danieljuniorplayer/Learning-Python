l = float(input('Digite a largura da parede:'))
a = float(input('Digite a altura da parede:'))
m2 = l*a
print(f'Sua parede tem a dimensão de {l:.0f}x{a:.0f} e sua área é de \033[32m{m2:.0f}m²\033[m')
litro = m2 / 2    # 1 litro de tinta consegue pintar 2m²
print(f'Para pintar essa parede, você precisará de \033[32m{litro:.0f}L\033[m de tinta')