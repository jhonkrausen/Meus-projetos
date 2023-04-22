from Conexao import *

class Autenticar:
    def getAutenticar(email, senha):
        conexao = Conexao.getConexao()
        mycursor = conexao.cursor()

        sql = "SELECT * FROM usuario WHERE email=%s and senha=%s;"
        val = (email, senha)   
        mycursor.execute(sql, val)
        
        resultado = mycursor.fetchone()
        try:
            if email in resultado and senha in resultado:
                print("Logado!")
        except:
            print("Email ou senha incorretos!")

        conexao.close()