from datetime import datetime #Importacao da biblioteca datetime
#classe contato e ultilização do metado datetime para visualizar data e hora

class Contato:
    def __init__(self,nome,telefone,email):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.criando_data = datetime.now() #data de agora
        self.atualizacao_data = datetime.now()
    


    def atualizar_contato(self,telefone = None, email= None):
        if telefone:
            self.telefone = telefone
        if email:
            self. email = email
        self.atualizacao_data = datetime.now()

    def __str__(self):
        return (f'Nome: {self.nome}\n'
                f'Telefone: {self.telefone}\n'
                f'Email: {self.email}\n'
                f"Criado Em:{self.criando_data.strftime('%Y/%m/%d %H:%M')}\n"
                f"Atualizado em: {self.atualizacao_data.strftime('%Y-%m-%d %H:%M')}\n"
                )
class Agenda:
    def __init__(self):
        self.contatos = {}   
                
    def adicionar_contato(self, nome, telefone, email):
        if nome in self.contatos:
            print('Já existe um contato com esse nome.')
        else:
            self.contatos[nome] = Contato(nome, telefone, email)
            print('Contato Adicionado Com Sucesso!')
 
    def remover_contato(self,nome):
        if nome in self.contatos :
            del self.contatos [nome]
            print('Contato removido com sucesso.')
        else:
            print('Contato não encontrato')

    def buscar_contato(self,nome):
        if nome in self.contatos:
            print(self.contatos[nome])
        else:
            print('Contato não encontrado.')

    def listar_contato(self):
        if self.contatos:
          for contato in self.contatos.values():
            print(contato)
            print('='*30)
        else:
            print('Agenda vazia.')

    def atualizar_contato(self, nome, telefone=None, email=None):
        if nome in self.contatos:
            self.contatos[nome].atualizar_contato(telefone, email)
            print('Contato atualizado com sucesso.')
        else:
            print('Contato não encontrado.')


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
         opcao = input('Escolha uma opção: ')

         if opcao == '1':
                nome = input('Nome:')
                telefone = input('Telefone:')
                email = input('Email:')
                self.adicionar_contato( nome, telefone, email)

         elif opcao == '2':
                nome = input('Nome do contato a ser removido:')
                self.remover_contato(nome)

         elif opcao == '3':
                nome = input('Nome do contato: ')
                self.buscar_contato(nome)

         elif opcao == '4':
                self.listar_contato()

         elif opcao == '5':
                nome = input('Nome do contato: ')
                telefone = input('Novo Telefone')
                email = input('Novo Email ')
                self.atualizar_contato(nome, telefone if telefone else None, email if email else None)

         elif opcao == '6':
                print('Saindo...')
                break

         else:
                print('Opção inválida, tente novamente.')



if __name__ == "__main__":
    agenda = Agenda()
    agenda.menu()