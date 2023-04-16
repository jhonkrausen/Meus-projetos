valor = float(input("Digite o valor do pão: "))
resultados = []
print("Panificadora pão de ontem - Tabela de preços")
for i in range(1, 51):
    resultados.append(valor * i)
    print(f"{i} - R$ {resultados[i-1]:.2f}")
