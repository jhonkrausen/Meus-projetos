
num = int(input("Digite um número inteiro: "))
numeros = []
primos = []
divisoes = 0
for i in range(1, num+1):
    numeros.append(i)
    
for i in range(1, len(numeros)+1):
    numero = numeros[i-1]
    nPrimo = 0
    for i in range(2, numero):
        if numero % i == 0:
            nPrimo = nPrimo + 1
    if nPrimo > 0:
        divisoes = divisoes + 1
    else:
        primos.append(numero)

print(f"os primos são {primos}")
print(f"os números foram dividos {divisoes} vezes")