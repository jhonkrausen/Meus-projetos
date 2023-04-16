while True:
    numero = int(input("Digite um número inteiro: "))
    nPrimo = 0

    for i in range(2, numero):
        if numero % i == 0:
            nPrimo = nPrimo + 1
            print(f"Divisível por: {i}")
    if nPrimo > 0 or numero == 1:
        print("Não é um número primo")
    else:
        print("É primo")