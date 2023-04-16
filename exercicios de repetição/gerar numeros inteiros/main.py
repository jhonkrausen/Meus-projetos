numero1 = int(input("Digite um número inteiro: "))
numero2 = int(input("Digite um número inteiro: "))
numeros = []
for i in range((numero1 + 1), numero2):
    print(i, end= ' ')
    numeros.append(i)

soma = sum(numeros)
print(f"\nA soma dos números é: {soma}")