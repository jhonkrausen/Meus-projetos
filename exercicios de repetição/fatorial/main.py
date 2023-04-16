while True:
    numero = int(input("Digite um número inteiro de 0 a 16: "))

    resultado = numero
    for i in range(1, numero):
        resultado = resultado * (numero-1)
        numero = numero-1
    print(resultado)
