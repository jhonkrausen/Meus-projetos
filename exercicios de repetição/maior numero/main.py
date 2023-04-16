numeros = [] 

for numero in range(1, 6):
    numeros.append(int(input("Digite um número: ")))

maiorNumero = numeros[0]

contagem = 1

while contagem < len(numeros):
    if numeros[contagem] > maiorNumero:
        maiorNumero = numeros[contagem]
    contagem = contagem + 1
        
print ("O maior número é " + str (maiorNumero))



