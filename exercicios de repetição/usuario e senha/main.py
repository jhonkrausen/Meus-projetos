def entraDados(): 
    usuario = input("USUÁRIO: ")
    senha = input("SENHA: ")

    while usuario == senha:
        print("A senha não pode ser igual ao usuário! digite novamente!")
        entraDados()
    else:
        print("USUÁRIO: ", usuario)
        print("SENHA: ", senha)
        entraDados()
    
entraDados()