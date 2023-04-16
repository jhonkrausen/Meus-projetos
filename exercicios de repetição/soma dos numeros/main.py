numeros = []

for numero in range(1, 6):
    numeros.append(int(input("Digite um número: ")))
soma = sum(numeros)
media = soma / len(numeros)
print(f"A soma dos números é: {soma}")
print(f"A média dos números é: {media}")