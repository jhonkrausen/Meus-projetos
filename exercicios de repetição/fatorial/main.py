def entraDados():
    try:
        entraDados.numero = int(input("Digite um número inteiro de 0 a 16: "))
        if entraDados.numero < 0 or entraDados.numero > 16:
           print("Número inválido! deve ser inteiro de 0 a 16!")
           entraDados()
        else:
            pass 
    except:
        print("Número inválido! deve ser inteiro de 0 a 16!")
        entraDados()

entraDados()
resultado = entraDados.numero
for i in range(1, entraDados.numero):
    resultado = resultado * (entraDados.numero-1)
    entraDados.numero = entraDados.numero-1
print(resultado)