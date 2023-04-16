while True:  
    numero = int(input("Digite um número inteiro: "))
    resultado = numero
    print(f"Fatorial de: {numero}")
    print(f"{numero}! = ", end= ' ')
    for i in range(1, numero+1):
        if numero > 1:
            print(f"{numero} .", end= ' ')
            resultado = resultado * (numero-1)
            numero = numero-1
        else:
            print(f"{numero} =", end= ' ')
        
    print(resultado)

    