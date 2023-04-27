from Usuario import *
from Conexao import *
from Cadastrar import *
from Autenticar import *

class Main():
    
    def options():
        print("----------------")
        print("1 - ENTRAR")
        print("2 - CADASTRAR")
        print("----------------")
        option = input()
        if option == "1":
            email = input("Email: ")
            senha = input("Senha: ")
            Autenticar.getAutenticar(email, senha)
        elif option == "2":
            nome = input("Digite seu nome: ")
            cpf = input("Digite seu cpf: ")
            email = input("Digite seu email: ")
            telefone = input("Digite seu telefone: ")
            senha = input("Digite sua senha: ")

            usuario = Usuario(nome, cpf, email, telefone, senha)
            Cadastrar.cadastraUsuario(usuario.get_nome(), usuario.get_cpf(), usuario.get_email(), usuario.get_telefone(), usuario.get_senha())
    
    print("---Bem vindo!---")
    while True:
        options()





   


   
