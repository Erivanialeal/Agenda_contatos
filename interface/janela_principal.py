#importanto o Tkinter
import tkinter as tk
from tkinter import Label
from funcionalidades.database import Database
from tkinter import messagebox
from tkinter import ttk



class ContatosApp:
    def __init__(self,root):
        #criando a janela principal.
        self.janela= root
        #Título da janela
        self.janela.title('Agenda De Contatos',)
        #tamanho da janela
        self.janela.geometry('900x800')
        #cor de fundo
        self.janela.configure(bg='light blue')
        # Configuração principal do grid da janela
        self.janela.grid_rowconfigure(0, weight=1)
        self.janela.grid_columnconfigure(0, weight=1)

        self.frame_principal=tk.Frame(self.janela,bg='light blue')
        self.frame_principal.grid(row=1,column=0,padx=20,pady=5,sticky='n')
        # Configurar grid do frame
        self.frame_principal.configure(width=600, height=700)  # Definir dimensões fixas
        self.frame_principal.grid_propagate(False)  # Impedir que o tamanho mude

        self.frame_tabela = tk.Frame(self.janela,height=50,bg='light blue')
        self.frame_tabela.grid(row=1, column=0, padx=20, pady=(20,0))
        self.frame_tabela.grid_rowconfigure(0, weight=1)
        self.frame_tabela.grid_columnconfigure(0, weight=1)

        self.frame_cima= tk.Frame(self.janela,bg='light blue',width=500,height=50,relief='flat')
        self.frame_cima.grid(row=0,column=0,sticky='nsew',pady=1,padx=0)
        


        self.Database= Database() #inicializando a classe Databases
        self.Database.conectar()
        self.funcionalidades()
        self.campo_adicionar()
        self.campo_remover()
        self.botao_listar()
        self.campo_atualizar()
        self.botao_sair()
    def ocultar_campos(self):
        #escondendo funcionalidades de adicionar Contato e botao salvar
        self.nome_label.grid_forget()
        self.nome_entry.grid_forget()
        self.label_email.grid_forget()
        self.email_entry.grid_forget()
        self.telefone_label.grid_forget()
        self.telefone_entry.grid_forget()
        self.botao_salvar.grid_forget()
        #escondendo funcionalidades de remover contato
        self.label_nome_remover.grid_forget()
        self.entry_nome_remover.grid_forget()
        self.botao_excluir.grid_forget()
        #escondendo funcionalidades de atualizar contato
        self.nome_atualizar.grid_forget()
        self.nome_entry_atualiza.grid_forget()
        self.telefone_atualizar.grid_forget()
        self.telefone_entry_atualizar.grid_forget()
        self.email_atualizar.grid_forget()
        self.email_entry_atualizar.grid_forget()
        self.botao_atualizar_confirmar.grid_forget()
        self.botao_atualizar_confirmar.grid_forget()
        self.label_barra_atualizar.grid_forget()
        self.entry_barra_atualizar.grid_forget()
        self.botao_buscar_atualizar.grid_forget()
        
        if hasattr(self, 'tree'):
            self.tree.grid_forget()
        
        

    def funcionalidades(self):
        label_pesquisar=tk.Label(self.frame_principal,text='Buscar',bg='Lavender',relief='sunken')
        label_pesquisar.grid(row=0,column=0,sticky='we',pady=5)

        self.barra_de_pesquisa=tk.Entry(self.frame_principal,width=15,bg='lavender',)
        self.barra_de_pesquisa.grid(row=0,column=1,columnspan=3,sticky='ew',pady=5)
        #adicionando um botão buscar
        botao_buscar=tk.Button(self.frame_principal,text='Buscar',bg='light green',command=self.buscar_contato)
        botao_buscar.grid(row=0,column=3,sticky='ew',pady=5)
        self.label_resultado = tk.Label(self.frame_principal,text='',fg='black',bg='light blue')
        self.label_resultado.grid(row=1,column=0,columnspan=3,sticky='ew',pady=10)
                                                                                                    #azul medio
        self.agenda_contatos=tk.Label(self.frame_cima,text="AGENDA DE CONTATOS.",font=('Ariel',15,"bold"),bg='#5DADE2',fg='black',width=73)
        self.agenda_contatos.grid(pady=10,sticky='nsew')

    def campo_adicionar(self):
        self.botao_adicionar= tk.Button(self.frame_principal,text='Adicionar Contato',bg='Lavender',command=self.mostrar_campos_adicionar)
        self.botao_adicionar.grid(row=2,column=0,pady=5,padx=5,sticky='ew')

        self.botao_salvar=tk.Button(self.frame_principal,text='Salva',bg='Lavender')

        #Entrada e label para nome.
        self.nome_label=tk.Label(self.frame_principal,text='Nome:',bg='Lavender',relief='sunken')
        self.nome_entry=tk.Entry(self.frame_principal, width=10,bg='Lavender')

        #Label e entrada telefone.
        self.telefone_label=tk.Label(self.frame_principal,text='Telefone:',bg='Lavender',relief='sunken')
        self.telefone_entry=tk.Entry(self.frame_principal,width=10,bg='Lavender')

        self.label_email=tk.Label(self.frame_principal,text='Email:',bg='Lavender',relief='sunken')
        self.email_entry= tk.Entry(self.frame_principal,width=10, bg='Lavender')

        self.botao_salvar = tk.Button(self.frame_principal, text='Salvar', bg='light green',width=10,command=self.salvar_contato)
    def mostrar_campos_adicionar(self):
        self.ocultar_campos()
        #mostrar compas de entrada e o botao salvar.
        self.nome_label.grid(row=3,column=0,pady=5,sticky='we')
        self.nome_entry.grid(row=3,column=1,pady=5,sticky='we') 

        self.telefone_label.grid(row=4,column=0,pady=5,sticky='we')
        self.telefone_entry.grid(row=4,column=1,pady=5,sticky='we') 

        self.label_email.grid(row=5,column=0,pady=5,sticky='we')
        self.email_entry.grid(row=5,column=1,pady=5,sticky='we')

        self.botao_salvar.grid(row=6,column=0,sticky='we')
        
    def limpar_campos(self):
        # Limpar os campos de entrada e esconder os campos de adicionar
        self.nome_entry.delete(0, tk.END)
        self.telefone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.entry_nome_remover.delete(0,tk.END)
        #escondendo os campos de adicionar
        self.nome_label.grid_remove()
        self.nome_entry.grid_remove()
        self.telefone_label.grid_remove()   
        self.telefone_entry.grid_remove()
        self.label_email.grid_remove()
        self.email_entry.grid_remove()
        self.botao_salvar.grid_remove()
        self.entry_nome_remover.grid_remove()
        self.label_nome_remover.grid_remove()
        self.botao_excluir.grid_remove()

    def campo_remover(self):
        self.botao_remover=tk.Button(self.frame_principal,text='Remover Contato',bg='Lavender',command=self.mostrar_campo_remover)
        self.botao_remover.grid(row=2,column=1,padx=5,pady=5,sticky='ew')

        self.label_nome_remover=tk.Label(self.frame_principal,text='Nome:', bg='Lavender',relief='sunken')
        self.entry_nome_remover=tk.Entry(self.frame_principal,bg='Alice Blue',width=10)

        self.botao_excluir=tk.Button(self.frame_principal,bg='#FF6666',text='Excluir',command=self.remover_contato)
        
    def mostrar_campo_remover(self):
        self.ocultar_campos()
        self.label_nome_remover.grid(row=3,column=1,sticky='ew',pady=5)
        self.entry_nome_remover.grid(row=3,column=2,sticky='ew',pady=5)
        self.botao_excluir.grid(row=3,column=3,sticky='ew',pady=5)

    def botao_listar(self):
        self.botao_listar=tk.Button(self.frame_principal,text='Listar Contatos',bg='Lavender',command=self.exibir_janela_listar)
        self.botao_listar.grid(row=2,column=2,padx=5,pady=5,sticky='ew')

    def exibir_janela_listar(self):
        
        self.ocultar_campos()
        self.tree=ttk.Treeview(self.frame_tabela,columns=('Nome', "Telefone", "Email"), show='headings')
        self.tree.heading('Nome', text='Nome',)
        self.tree.heading('Telefone', text='Telefone')
        self.tree.heading('Email', text='Email')
        self.tree.grid(row=0,column=0, sticky='nsew')

        scrollbar = ttk.Scrollbar(self.frame_tabela, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.listar_contato()
        
    def campo_atualizar(self):
        self.atualizar=tk.Button(self.frame_principal,text='Atualizar',bg='lavender',command=self.mostrar_campo_atualizar)
        self.atualizar.grid(row=2,column=3,padx=5,pady=5)

        self.nome_atualizar=tk.Label(self.frame_principal,text='Atualizar Nome:',bg='lavender',relief='sunken')
        self.nome_entry_atualiza=tk.Entry(self.frame_principal,bg='Alice Blue',width=10)
        self.telefone_atualizar=tk.Label(self.frame_principal,text='Atualizar Telefone:',bg='Lavender',relief='sunken')
        self.telefone_entry_atualizar=tk.Entry(self.frame_principal,bg='Alice Blue',width=10)
        self.email_atualizar=tk.Label(self.frame_principal,text='Atualizar Email',bg='lavender',relief='sunken')
        self.email_entry_atualizar=tk.Entry(self.frame_principal,bg='Alice Blue',width=10)
        # Label e entrada de buscar contato para atualizar.
        self.label_barra_atualizar=tk.Label(self.frame_principal,text='Atualizar Contato:',bg='Lavender',relief='sunken')
        self.entry_barra_atualizar=tk.Entry(self.frame_principal,bg='Alice Blue',width=10)
        self.botao_buscar_atualizar=tk.Button(self.frame_principal,text='Buscar',bg='light green',width=10,command=self.buscar_contato_atualizar)

        self.botao_atualizar_confirmar=tk.Button(self.frame_principal,text='Confirmar!',bg='light green',command=self.atualizar_contato)

    def mostrar_campo_atualizar(self):
        self.ocultar_campos()
        self.label_barra_atualizar.grid(row=3,column=3,pady=5,sticky='ew')
        self.entry_barra_atualizar.grid(row=3,column=4,pady=5,sticky='ew')
        self.botao_buscar_atualizar.grid(row=3,column=5,sticky='ew')

        self.telefone_atualizar.grid(row=4,column=3,pady=5,sticky='ew')
        self.telefone_entry_atualizar.grid(row=4,column=4,pady=5,sticky='ew')
        self.email_atualizar.grid(row=5,column=3,pady=5,sticky='ew')
        self.email_entry_atualizar.grid(row=5,column=4,pady=5,sticky='ew')

        self.botao_atualizar_confirmar.grid(row=6,column=4,pady=5,sticky='ew')

    def atualizar_contato(self):
        nome=self.nome_entry_atualiza.get() # nome como chave para buscar o contato.
        telefone=self.telefone_entry_atualizar.get()
        email=self.email_entry_atualizar.get()
        if self.Database.atualizar_contato(nome,telefone,email):
            self.atualizar_tabela()
            
            tk.messagebox.showinfo('ATUALIZADO!',f'Contato atualizado: f\n Nome= {nome} \n Telefone= {telefone} \n Email= {email}')
        else:
            tk.messagebox.showerror('Erro',f'Erro ao atualizar contato {nome}')
        self.exibir_janela_listar()
            

    def botao_sair(self):
        self.botao_sair=tk.Button(self.frame_principal,text='SAIR.',bg='pink',command=self.sair,width=10)
        self.botao_sair.grid(row=10,column=1,pady=50,sticky='ew',)
    def buscar_contato(self):
        nome= self.barra_de_pesquisa.get().strip()
        resultado=self.Database.buscar_contato(nome) 

        
        if  resultado:
            #acessando os resultados 
            self.label_resultado.config( text=f'Contato encontrado.\n Nome: {resultado["nome"]}\n Telefone: {resultado["telefone"]}\n Email: {resultado["email"]}')
        else:
            self.label_resultado.config(text=f'Contato não encontrado')

    def salvar_contato(self):
        nome=self.nome_entry.get()
        telefone=self.telefone_entry.get()
        email=self.email_entry.get()
        if nome and telefone and email:
            resultado= self.Database.adicionar_contato(nome,telefone,email)
            resultado=True
            if resultado:
                tk.messagebox.showinfo('Sucesso',f'Contato {nome} adicionado com sucesso!')
                self.limpar_campos()
            else:
                tk.messagebox.showerror('Erro', 'Erro ao adicionar contato')
        else:
            tk.messagebox.showwarning('Atenção','Por Favor,preecha todos os campos.') 

    def remover_contato(self):
        nome=self.entry_nome_remover.get()
        if nome:
            confirma= messagebox.askyesno("Confirmação", f"Tem certeza que deseja excluir o contato {nome}?")
            if confirma:
                db=Database()
                sucesso= db.remover_contato(nome)
                if sucesso:
                    messagebox.showinfo('Sucesso',f'Contato {nome} removido com sucesso!')
                    self.limpar_campos()
                else:
                    messagebox.showerror('Erro', 'Erro ao remover o contato')
            else:
                messagebox.showinfo('Cancelado', 'A remoção foi cancelada.')

    def listar_contato(self):
        db=Database()
        resultado=db.listar_contato()
        # Limpa o Treeview antes de inserir novos dados 
        for item in self.tree.get_children():
            self.tree.delete(item)

        for contato in resultado:
            id_contato,nome,telefone,email= contato
            self.tree.insert("", "end", values=(nome,telefone,email))

    def buscar_contato_atualizar(self):
        nome=self.entry_barra_atualizar.get()
        resultado=self.Database.buscar_contato(nome)
        if resultado:
            self.nome_entry_atualiza.delete(0, tk.END)
            self.nome_entry_atualiza.insert(0, nome)
            self.telefone_entry_atualizar.delete(0, tk.END)
            self.telefone_entry_atualizar.insert(0, resultado['telefone'])
            self.email_entry_atualizar.delete(0, tk.END)
            self.email_entry_atualizar.insert(0, resultado['email'])
        else:
            messagebox.showinfo('Contato encontrado.')

    def atualizar_tabela(self):

    # Recriar a tabela com os dados atualizados
        row = 0
        contatos= self.Database.listar_contato()
        print(self.Database.listar_contato())
        for contato in contatos:
            telefone = contato[2]
            email = contato[3]
   
    def sair(self):
        self.Database.sair()
        self.janela.destroy() #fecha a janela do tkinter
