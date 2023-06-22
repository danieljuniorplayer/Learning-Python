l = float(input('Digite a largura da parede:'))
a = float(input('Digite a altura da parede:'))
m2 = l*a
print(f'Sua parede tem a dimensão de {l}x{a} e sua área é de {m2}m²')
litro = m2 / 2    # 1 litro de tinta consegue pintar 2m²
print(f'Para pintar essa parede, você precisará de {litro}L de tinta')