numero = int(input("Digite um número inteiro: "))
resultados = []
for i in range(1, 11):
    resultados.append(numero * i)
    print(f"{i} X {numero} = {resultados[i-1]}")