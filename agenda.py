from contato import Contato

class Agenda:
    def __init__(self):
        #inicializa a classe Agenda, e cria uma instancia de Bancodedados.
        self.lista_de_contatos = {}
                
    def adicionar_contato(self, nome, telefone, email):

        nome = nome.lower().strip()
        telefone = telefone.strip().lower()
        email = email.strip().lower()

        if nome in self.lista_de_contatos:
            return f'já existe um contato com esse nome.'
        else:
            self.lista_de_contatos[nome] = Contato(nome,telefone,email)
        return f'Contato {nome} adicionando com sucesso'
        
 
    def remover_contato(self,nome):
        nome = nome.strip()
        print(f"Tentando remover o contato : {nome}") #Debug para verificar o nome.
        if nome in self.lista_de_contatos :
            del self.lista_de_contatos [nome]
            return 'Contato removido com sucesso'

    def buscar_contato(self,nome):
        nome = nome.lower()
        nome = nome.strip()
        if nome in self.lista_de_contatos:
             return self.lista_de_contatos[nome]
        else:
            return f'Contato {nome} não encontrado'
             
    def listar_contato(self):
        if self.lista_de_contatos:
             for con in self.lista_de_contatos.values():
                return con
        else:
             return 'Agenda vazia'
        
    def atualizar_contato(self,nome,telefone=None,email=None):
        if nome in self.lista_de_contatos:
            self.lista_de_contatos[nome].atualizar_contato(telefone,email)
            return 'Contato atualizado com sucesso'
        else:
             return 'Contato não encontrado'
         

   
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



