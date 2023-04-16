notas = []

nNotas = int(input("Quantas notas você tem?: "))

for i in range(1, nNotas+1):
    notas.append(int(input(f"Digite a nota {i}: ")))

soma = sum(notas)
media = soma/len(notas)

print(f"A média das suas notas é: {media:.1f}")