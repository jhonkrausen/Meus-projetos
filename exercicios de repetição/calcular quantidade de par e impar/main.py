numeros = []
pares = []
impares = []

for x in range(1,11):
    numeros.append(int(input("Digite um número: ")))

for i in range(1, 11):
    if (numeros[i-1] % 2) == 0:
        pares.append(numeros[i-1])
    else:
        impares.append(numeros[i-1])

print(f"os números pares são: {pares}", end = ' ')
print(f"\nos números impares são: {impares}", end = ' ')

