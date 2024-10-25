#from .contato import Contato
from .database import Database

class Agenda:
    def __init__(self):
        #inicializa a classe Agenda, e cria uma instancia de Bancodedados.
        self.banco = Database()
                
    def adicionar_contato(self, nome, telefone, email):
        #padronizar entrada
        try:
            nome = nome.lower().strip()
            telefone = telefone.strip().lower()
            email = email.strip().lower()

            if self.banco.adicionar_contato(nome,telefone,email):
                return f'Contato {nome} adicionando com sucesso'
            else:
                 return f'Fanha ao adicionar o contato {nome}'
        except  Exception as e:
            return f'Ocorreu um erro ao adicionar o contato: {e}' 
 
    def remover_contato(self,nome):
        #usando o try: e o except: para tratar possiveis erros.
        try:
            nome = nome.strip().lower()
            print(f"Tentando remover o contato : {nome}") #Debug para verificar o nome.
            if self.banco.remover_contato(nome):
                return f'Contato {nome} removido com sucesso'
            else:
                 return f'Contato {nome} não encontrado'
        except Exception as e:
             return f'Erro ao remover contato'
             

    def buscar_contato(self,nome):
        nome = nome.lower().strip()

        try:
            contato = self.banco.buscar_contato(nome)

            if contato and len (contato) > 0: #verifica se a lista de contatos não está vazia
                print (f'Contato encontrado: {contato[0]}') #Exibe o primeiro contato encotrado

        except Exception as e:
            print (f'Erro ao buscar contato {e}.')
             
    def listar_contato(self):
        try:
            contatos = self.banco.listar_contato()
            if contatos:
                # o .join está sendo usado para tranformar os elementos em contato em string
                return '\n'.join([str(contato) for contato in contatos])
            else:
                return 'Agenda vazia'
        except Exception as e:
            return f'Erro ao listar contatos: {e}'
        
    def atualizar_contato(self, nome, telefone=None, email=None):
        nome = nome.lower().strip()

        try:
            if self.banco.atualizar_contato(nome, telefone, email):
                return f'Contato {nome} atualizado com sucesso'
            else:
                return
        except Exception as e:
            return f'Erro ao atualizar contato: {e}'

   
    def menu(self):
     

     menu_txt = '''
    ========================
    1. Adicionar Contato
    2. Remover Contato
    3. Buscar Contato
    4. Listar Todos Os Contatos
    5. Atualizar Contato
    6. Sair
    ========================
    '''

     while True:
         print(menu_txt)
         opcao = input('Escolha uma opção:')

         if opcao == '1':
                nome = input('Nome:')
                telefone = input('Telefone:')
                email = input('Email:')
                print(self.adicionar_contato(nome,telefone,email))

         elif opcao == '2':
                nome = input('Nome do contato a ser removido:')
                print(self.remover_contato(nome))

         elif opcao == '3':
                nome = input('Nome do contato: ')
                print(self.buscar_contato(nome))

         elif opcao == '4':
                print(self.listar_contato())

         elif opcao == '5':
                nome = input('Nome do contato: ')
                telefone = input('Novo Telefone:')
                email = input('Novo Email: ')
                print(self.atualizar_contato(nome, telefone if telefone else None, email if email else None))

         elif opcao == '6':
                print('Saindo...')
                break

         else:
                print('Opção inválida, tente novamente.')



