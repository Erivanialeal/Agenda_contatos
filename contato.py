from datetime import datetime
 #Importacao da biblioteca datetime
#classe contato e ultilização do metado datetime para visualizar data e hora

class Contato:
    #definindo as variáveis de instância
    def __init__(self,nome,telefone,email):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.criando_data = datetime.now() #data de agora
        self.atualizacao_data = datetime.now()
    
    def atualizar_contato(self,telefone = None, email= None):
        if telefone:
            self.telefone = telefone #atualiza o telefone
        if email:
            self. email = email #atualiza o email
        self.atualizacao_data = datetime.now() #atualiza a data e a hora 

    def __str__(self):
        #retornando as representação em string de cada variável.
        return (f'Nome: {self.nome}\n'
                f'Telefone: {self.telefone}\n'
                f'Email: {self.email}\n'
                f"Criado Em:{self.criando_data.strftime('%Y/%m/%d %H:%M')}\n"
                f"Atualizado em: {self.atualizacao_data.strftime('%Y-%m-%d %H:%M')}\n"
                )