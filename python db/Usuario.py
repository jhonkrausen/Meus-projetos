class Usuario:

    def __init__(self, nome, cpf, email, telefone, senha):
        self.set_nome(nome)
        self.set_cpf(cpf)
        self.set_email(email)
        self.set_telefone(telefone)
        self.set_senha(senha)
        
    def set_nome(self, nome):
        self._nome = nome

    def get_nome(self):
        return self._nome
    
    def set_cpf(self, cpf):
        self._cpf = cpf

    def get_cpf(self):
        return self._cpf
    
    def set_email(self, email):
        self._email = email

    def get_email(self):
        return self._email
    
    def set_telefone(self, telefone):
        self._telefone = telefone

    def get_telefone(self):
        return self._telefone
    
    def set_senha(self, senha):
        self._senha = senha

    def get_senha(self):
        return self._senha
