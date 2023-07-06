soma =0
for c in range(1,501):  # entre 1 e 500
    if c % 2 == 1:      # numeros ímpares
        if c % 3 == 0:  # e multiplos de 3
            soma += c   # soma todos eles
print(soma)
# alternativo
soma =0
qtd = 0
for c in range(1,501,2):  # entre 1 e 500 # numeros ímpares
        if c % 3 == 0:  # e multiplos de 3
            soma += c   # soma todos eles
            qtd +=1

print(soma)
print(qtd)
