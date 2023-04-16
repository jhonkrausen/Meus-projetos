numeros = []
x = 11
i = 1
while i < x:
    numero = int(input("Digite um número: "))
    if numero >= 0 and numero <= 1000:
        numeros.append(numero)
    else:
        print("O número deve estar entre 0 e 1000!")
        x = x + 1
    i = i + 1

maiorNumero = numeros[0]
menorNumero = numeros[0]

contagem = 1

while contagem < len(numeros):
    if numeros[contagem] > maiorNumero:
        maiorNumero = numeros[contagem]
    if numeros[contagem] < menorNumero:
        menorNumero = numeros[contagem]
    contagem = contagem + 1
soma = maiorNumero + menorNumero

print(numeros)
print(f"O maior número é: {maiorNumero}")
print(f"O menor número é: {menorNumero}")
print(f"A soma deles é: {soma}")