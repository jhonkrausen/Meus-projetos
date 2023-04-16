n = int(input("Digite o enésimo termo: "))
fibonacci = [0,1]

for i in range(1, n-1):
    soma = fibonacci[i-1] + fibonacci[i]
    fibonacci.append(soma)

print(soma)