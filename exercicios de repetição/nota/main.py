
def entraDados():
    entraDados.nota = float
    try:
        entraDados.nota = float(input("Digite uma nota entre 0 a 10: "))
        validaDados()
    except:
        print("Você deve digitar um valor numérico!")
        entraDados()

def validaDados():

    while entraDados.nota < 0 or entraDados.nota > 10:
        entraDados()
entraDados()