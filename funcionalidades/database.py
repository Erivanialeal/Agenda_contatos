import sqlite3

class Database:
    #função conectar para evitar a repetição de codigo nas outras funções
    def conectar(self):
        """Função para criar e retornar a conexão e o cursor."""
        conexão = sqlite3.connect('sqlite/meu_banco.db')
        cursor = conexão.cursor()
        return conexão, cursor

    def tabela(self):
        conexão, cursor = self.conectar()

        #comando SQL para criar a tabela
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS agenda ( 
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                telefone TEXT NOT NULL,
                email TEXT 
        )
    ''')
        conexão.commit() #salvando as informaçoes no banco de dados
        #fechar conexão
        conexão.close()



    def adicionar_contato(self,nome, telefone, email):
        conexão, cursor = self.conectar()
        try:
        #inserindo informações no banco
            cursor.execute('''
                INSERT INTO agenda (nome, telefone, email)
                VALUES (? , ? , ? );
        ''', (nome, telefone , email))
        
            conexão.commit()
            return f'Contato {nome} adicionado com sucesso'
            return True # True para indicar que a inserção foi bem sucedida
        except Exception as e:
            return f'Erro ao adicionar contato: {e}:'
            return False
        finally:
            cursor.close()
            conexão.close()


    
    def remover_contato(self, nome):
        conexão, cursor = self.conectar()
        try:
            # Verifica se o contato existe antes de remover
            cursor.execute('''
                SELECT * FROM agenda
                WHERE LOWER(nome) = LOWER(?);
            ''', (nome,))
            resultado = cursor.fetchone()

            if resultado:  # Se o contato existe
                cursor.execute('''
                    DELETE FROM agenda
                    WHERE LOWER(nome) = LOWER(?);
                ''', (nome,))
                conexão.commit()  # Commit para salvar as mudanças

                return f'Contato {nome} removido com sucesso!'
            else:
                return f'Contato {nome} não encontrado!'

        except Exception as e:
            return f'Ocorreu um erro ao remover o contato: {e}'
        finally:
            cursor.close()  # Fecha o cursor
            conexão.close()  # Fecha a conexão


    def buscar_contato(self,nome):
        conexão ,cursor = self.conectar()
        try:
            nome = nome.lower().strip() #remover espaços antes e depois do nome
            cursor.execute('''
                SELECT * FROM agenda
                WHERE LOWER(nome) = LOWER (?);
            ''',(nome,))

            resultado = cursor.fetchall() #usar fechall para pegar todos os resultados
            

            if resultado:
                for contato in resultado:
                    print('contato encontrado:',contato) #impre os detalhes do contato

            else:
                return f'Contato {nome} não encontrado.'

        except Exception as e:
            print(f'Erro ao buscar {e}.')
        
        finally:
    
            cursor.close()
            conexão.close()

    def listar_contato(self): 
        conexão, cursor = self.conectar()

        try:
            cursor.execute('SELECT * FROM  agenda;')
            contatos = cursor.fetchall() #obtém todos os resultados da consulta e os armazena na variável contatos
            return contatos
        
        finally:
            cursor.close()
            conexão.close()
    
    def atualizar_contato(self, nome, telefone = None , email= None):
        conexão , cursor = self.conectar()
        try:
            nome = nome.lower().strip()

            cursor.execute('''
                SELECT id, nome , telefone , email
                FROM agenda
                WHERE LOWER(nome) = LOWER(?);

        ''',(nome,))
            contatos= cursor.fetchall()

            if not contatos: #se não houver contato correspondente
                return
            #Exibindo contatos encontrados
            return 'Contatos encontrados:'
        
            for contato in contatos:
                print(f'ID {contato[0]} nome {contato[1]} telefone {contato[2]} email {contato[3]}')

            # atualizando telefone se fornecido.
            if telefone is not None:
                cursor.execute('''
                UPDATE agenda
                SET telefone = ?
                WHERE LOWER(nome) = LOWER(?);
            ''',(telefone,nome))
                print(f'Telefone atualizado para {telefone}')

            if email is not None:
                cursor.execute('''
                    UPDATE agenda
                    SET email = ?
                    WHERE LOWER(nome) =  LOWER(?);
            ''',(email,nome))
                print(f'Email atualizado para {email}')

                conexão.commit()
                print("Contato atualizado com sucesso.")
            
        except Exception as e:

            print(f'Erro ao atualizar contato {e}')

            cursor.close()
            conexão.close()

db=Database()
db.tabela()
db.adicionar_contato('nome', 'telefone', 'email')
db.remover_contato('nome')
#a função buscar_contato e listar_contato precisa está sendo armazenadas por 
#uma variável pois elas buscam resultados que podem ser ultilizados posteriomente.
contato = db.buscar_contato('nome')
todos_os_contatos = db.listar_contato()
db.atualizar_contato('nome', 'telefone', 'email')