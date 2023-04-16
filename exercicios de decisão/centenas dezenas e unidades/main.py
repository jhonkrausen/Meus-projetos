def entraDados():
    numero = input('Digite um número de "0" a "999": ')
    centena = int
    dezena = int
    unidade = int

    if len(numero) == 3:
        centena = int(numero[0])
        dezena = int(numero[1])
        unidade = int(numero[2])

        if centena < 2 and dezena < 2 and unidade < 2:
            print("Esse número tem " + str(centena) + " centena e " + str(dezena)+ " dezena e " + str(unidade) + " unidade")

        elif centena < 2 and dezena < 2 and unidade >= 2:
            print("Esse número tem " + str(centena) + " centena e " + str(dezena)+ " dezena e " + str(unidade) + " unidades")

        elif centena < 2 and dezena >= 2 and unidade < 2:
            print("Esse número tem " + str(centena) + " centena e " + str(dezena)+ " dezenas e " + str(unidade) + " unidade")

        elif centena < 2 and dezena >=2 and unidade >= 2:
            print("Esse número tem " + str(centena) + " centena e " + str(dezena)+ " dezenas e " + str(unidade) + " unidades")

        elif centena >= 2 and dezena < 2 and unidade < 2:
            print("Esse número tem " + str(centena) + " centenas e " + str(dezena)+ " dezena e " + str(unidade) + " unidade")

        elif centena >= 2 and dezena < 2 and unidade >= 2:
            print("Esse número tem " + str(centena) + " centenas e " + str(dezena)+ " dezena e " + str(unidade) + " unidades")

        elif centena >= 2 and dezena >= 2 and unidade < 2:
            print("Esse número tem " + str(centena) + " centenas e " + str(dezena)+ " dezenas e " + str(unidade) + " unidade")

        elif centena >= 2 and dezena >=2 and unidade >= 2:
            print("Esse número tem " + str(centena) + " centenas e " + str(dezena)+ " dezenas e " + str(unidade) + " unidades")

    elif len(numero) == 2:
        dezena = int(numero[0])
        unidade = int(numero[1])

        if dezena < 2 and unidade < 2:
            print("Esse número tem " + str(dezena)+ " dezena e " + str(unidade) + " unidade")

        elif dezena < 2 and unidade >= 2:
            print("Esse número tem " + str(dezena)+ " dezena e " + str(unidade) + " unidades")

        elif dezena >= 2 and unidade < 2:
            print("Esse número tem " + str(dezena)+ " dezenas e " + str(unidade) + " unidade")

        else:
            print("Esse número tem " + str(dezena)+ " dezenas e " + str(unidade) + " unidades")

    elif len(numero) == 1:
        unidade = int(numero[0])

        if unidade < 2:
            print("Esse número tem " + str(unidade) + " unidade")

        else:
            print("Esse número tem " + str(unidade) + " unidades")
    entraDados()
entraDados()