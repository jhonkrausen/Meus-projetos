base = int(input("Digite o número base: "))
expoente = int(input("Digite o número expoente: "))
resultado = base
for i in range(1, expoente):
    resultado = resultado * base
print(resultado)