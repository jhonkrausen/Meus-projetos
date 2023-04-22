import mysql.connector

class Conexao:
    
    def getConexao():
        conexao = mysql.connector.connect(host='localhost', user='Jhonatan', password='bjpk3009', database='db_teste')
        return conexao
    
 
        



