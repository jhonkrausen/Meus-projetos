print("---------------------------------------------------------")
print("---CARNE----------ATÉ 5KG----------ACIMA DE 5KG----------")
print(" 1 FILE DUPLO  R$ 4,90 POR KG     R$ 5,80 POR KG         ")
print(" 2 ALCATRA     R$ 5,90 POR KG     R$ 6,80 POR KG         ")
print(" 3 PICANHA     R$ 6,90 POR KG     R$ 7,80 POR KG         ")
print("---------------------------------------------------------")
print("---------APENAS UM TIPO DE CARNE POR CLIENTE!------------")
print("------RECEBA 5% DE DESCONTO EM COMPRAS NO CARTÃO!--------")
print("---------------------------------------------------------")
carnes = {
    "Filé Duplo": 0,
    "Alcatra": 0,
    "Picanha": 0
}
def main():
    main.carne = input("Escolha uma carne: ")
    escolhendoCarnes()

def escolhendoCarnes():
    if main.carne == "1":
        try: 
            escolhendoCarnes.kg = float(input("Quantos kg?: "))
        except:
            print("Valor inválido! digite novamente!")
            escolhendoCarnes()
        carnes["Filé Duplo"] = escolhendoCarnes.kg

    elif main.carne == "2":
        try: 
            escolhendoCarnes.kg = float(input("Quantos kg?: "))
        except:
            print("Valor inválido! digite novamente!")
            escolhendoCarnes()
        carnes["Alcatra"] = escolhendoCarnes.kg
    elif main.carne == "3":
        try: 
            escolhendoCarnes.kg = float(input("Quantos kg?: "))
        except:
            print("Valor inválido! digite novamente!")
            escolhendoCarnes()
        carnes["Picanha"] = escolhendoCarnes.kg
    else:
        print("Escolha entre 1 e 2!")
        main()
    metodoPagamento()

def metodoPagamento():
    metodoPagamento.cartaoOk = False
    metodoPagamento.escolha = input("Quer pagar no cartão? S/N: ")
    if metodoPagamento.escolha == "S" or metodoPagamento.escolha == "s":
        metodoPagamento.cartaoOk = True
        calculaValor()
    elif metodoPagamento.escolha == "N" or metodoPagamento.escolha == "n":
        metodoPagamento.cartaoOk = False
        calculaValor()
    else:
        print("Não entendi, por favor, digite novamente!")
        metodoPagamento()

def calculaValor():
    calculaValor.desconto = bool
    calculaValor.valorFileduplo = float
    calculaValor.valorAlcatra = float
    calculaValor.valorPicanha = float
    calculaValor.valorTotal = float
    calculaValor.valorLiquido = float
    calculaValor.pesoTotal = carnes["Alcatra"] + carnes["Filé Duplo"] + carnes["Picanha"]

    if carnes["Filé Duplo"] <= 5:
        calculaValor.valorFileduplo = carnes["Filé Duplo"] * 4.90
    else:
        calculaValor.valorFileduplo = carnes["Filé Duplo"] * 5.80  

    if carnes["Alcatra"] <= 5:
        calculaValor.valorAlcatra = carnes["Alcatra"] * 5.90
    else:
        calculaValor.valorAlcatra = carnes["Alcatra"] * 6.80

    if carnes["Picanha"] <= 5:
        calculaValor.valorPicanha = carnes["Picanha"] * 6.90
    else:
        calculaValor.valorPicanha = carnes["Picanha"] * 7.80


    calculaValor.valorTotal = calculaValor.valorAlcatra + calculaValor.valorFileduplo + calculaValor.valorPicanha

    if metodoPagamento.cartaoOk == True:
        calculaValor.valorLiquido = calculaValor.valorTotal * 0.95
        calculaValor.desconto = True
    else:
        calculaValor.valorLiquido = calculaValor.valorTotal

    prints()

def prints():
    print("----------------------------------------------------------------------------------")
    if carnes["Filé Duplo"] > 0:
        print(f"Você comprou {carnes['Filé Duplo']} kg de Filé Duplo por R$ {calculaValor.valorFileduplo:.2f}")

    if carnes["Alcatra"] > 0:
        print(f"Você comprou {carnes['Alcatra']} kg de Alcatra por R$ {calculaValor.valorAlcatra:.2f}")
    
    if carnes["Picanha"] > 0:
        print(f"Você comprou {carnes['Picanha']} kg de Picanha por R$ {calculaValor.valorPicanha:.2f}")
    print("----------------------------------------------------------------------------------")
    if calculaValor.desconto == True:
        print(f"O valor total é: R$ {calculaValor.valorTotal:.2f}")
        print(f"Você recebeu 5% de desconto no cartão e pagará R$ {calculaValor.valorLiquido:.2f}")
    else:
        print(f"Você pagará o valor total de R$ {calculaValor.valorTotal:.2f}")
    carnes["Alcatra"] = 0
    carnes["Filé Duplo"] = 0
    carnes["Picanha"] = 0

    main()
    print("----------------------------------------------------------------------------------")
main()
