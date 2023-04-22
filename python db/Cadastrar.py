from Conexao import *

class Cadastrar:
    def cadastraUsuario(nome, cpf, email, telefone, senha):
        conexao = Conexao.getConexao()
        mycursor = conexao.cursor()

        sql = "INSERT INTO usuario(nome, cpf, email, telefone, senha) VALUES (%s, %s, %s, %s, %s);"
        val = (nome, cpf, email, telefone, senha)   
        mycursor.execute(sql, val)
        conexao.commit()
        conexao.close()
        print("INSERIDO!")