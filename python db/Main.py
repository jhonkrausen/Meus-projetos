from Usuario import *
from Conexao import *
from Cadastrar import *
from Autenticar import *

class Main():
    nome = input("Digite seu nome: ")
    cpf = input("Digite seu cpf: ")
    email = input("Digite seu email: ")
    telefone = input("Digite seu telefone: ")
    senha = input("Digite sua senha: ")

    usuario = Usuario(nome, cpf, email, telefone, senha)
    Cadastrar.cadastraUsuario(usuario.get_nome(), usuario.get_cpf(), usuario.get_email(), usuario.get_telefone(), usuario.get_senha())

    email = input("Email: ")
    senha = input("Senha: ")

    Autenticar.getAutenticar(email, senha)



   
