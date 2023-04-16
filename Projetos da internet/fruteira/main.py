print("---------------------------------------------------------")
print("---FRUTA----------ATÉ 5KG----------ACIMA DE 5KG----------")
print(" 1 MORANGO     R$ 2,50 POR KG     R$ 2,20 POR KG         ")
print(" 2 MAÇÃ        R$ 1,80 POR KG     R$ 1,50 POR KG         ")
print("---------------------------------------------------------")
frutas = {
    "Morango": 0,
    "Maçã": 0,
}
def main():
    main.fruta = input("Escolha uma fruta: ")
    escolhendoFrutas()

def escolhendoFrutas():
    if main.fruta == "1":
        try: 
            escolhendoFrutas.kg = float(input("Quantos kg?: "))
        except:
            print("Valor inválido! digite novamente!")
            escolhendoFrutas()
        frutas["Morango"] = escolhendoFrutas.kg

    elif main.fruta == "2":
        try: 
            escolhendoFrutas.kg = float(input("Quantos kg?: "))
        except:
            print("Valor inválido! digite novamente!")
            escolhendoFrutas()
        frutas["Maçã"] = escolhendoFrutas.kg
    else:
        print("Escolha entre 1 e 2!")
        main()
    maisFrutas()

def maisFrutas():
    maisFrutas.escolha = input("Quer mais frutas? S/N: ")
    if maisFrutas.escolha == "S" or maisFrutas.escolha == "s":
        main()
    elif maisFrutas.escolha == "N" or maisFrutas.escolha == "n":
        calculaValor()
    else:
        print("Não entendi, por favor, digite novamente!")
        maisFrutas()

def calculaValor():
    calculaValor.desconto = bool
    calculaValor.valorMorango = float
    calculaValor.valorMaca = float
    calculaValor.valorTotal = float
    calculaValor.valorLiquido = float
    calculaValor.pesoTotal = frutas["Maçã"] + frutas["Morango"]

    if frutas["Morango"] <= 5:
        calculaValor.valorMorango = frutas["Morango"] * 2.50
    else:
        calculaValor.valorMorango = frutas["Morango"] * 2.20  

    if frutas["Maçã"] <= 5:
        calculaValor.valorMaca = frutas["Maçã"] * 1.80
    else:
        calculaValor.valorMaca = frutas["Maçã"] * 1.50

    calculaValor.valorTotal = calculaValor.valorMaca + calculaValor.valorMorango

    if calculaValor.valorTotal > 25 or calculaValor.pesoTotal > 8:
        calculaValor.valorLiquido = calculaValor.valorTotal * 0.90
        calculaValor.desconto = True
    else:
        calculaValor.valorLiquido = calculaValor.valorTotal

    prints()

def prints():
    print("----------------------------------------------------------------------------------")
    if frutas["Morango"] > 0:
        print(f"Você comprou {frutas['Morango']} kg de morango por R$ {calculaValor.valorMorango:.2f}")

    if frutas["Maçã"] > 0:
        print(f"Você comprou {frutas['Maçã']} kg de maçã por R$ {calculaValor.valorMaca:.2f}")
    print("----------------------------------------------------------------------------------")
    if calculaValor.desconto == True:
        print(f"O valor total é: R$ {calculaValor.valorTotal:.2f}")
        print(f"Você recebeu 10% de desconto e pagará R$ {calculaValor.valorLiquido:.2f}")
    else:
        print(f"Você pagará o valor total de R$ {calculaValor.valorTotal:.2f}")
    maisFrutas()
    print("----------------------------------------------------------------------------------")
main()





