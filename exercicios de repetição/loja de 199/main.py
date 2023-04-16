numero = 1.99
resultados = []
print("Lojas Quase Dois - Tabela de preços")
for i in range(1, 51):
    resultados.append(numero * i)
    print(f"{i} - R$ {resultados[i-1]:.2f}")
