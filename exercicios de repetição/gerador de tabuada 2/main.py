numero = int(input("Digite um número inteiro: "))
tabuadaInicial = int(input("Digite onde a tabuada começará: "))
tabuadaFinal = int(input("Digite onde a tabuada terminará: "))
resultados = []
if tabuadaFinal > tabuadaInicial:
    x = 0
    for i in range(tabuadaInicial, tabuadaFinal+1):
        resultados.append(numero * i)
        x = x + 1
        print(f"{i} X {numero} = {resultados[x-1]}")
else:
    print("O final não pode ser menor que o inicio!")