from calendar import *

def entraDados():
    try:
        entraDados.ano = int(input("Digite um ano: "))
        calculaAno()
    except:
        print('Isso não é um ano!, "2023" é um ano')
        print("Digite novamente!")
        entraDados()

def calculaAno():
    if isleap(entraDados.ano):
        print(f"{entraDados.ano} é um ano bissexto")
    else:
        print(f"{entraDados.ano} não é um ano bissexto")
    entraDados()
    
entraDados()

