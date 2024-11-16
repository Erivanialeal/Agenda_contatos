from funcionalidades.agenda import Agenda
from funcionalidades.database import Database
from interface.janela_principal import ContatosApp
import tkinter as tk
if __name__ == "__main__":
    agenda = Agenda()
    database = Database()
    janela= tk.Tk()
    app=ContatosApp(janela)
    janela.mainloop()
    agenda.menu()
