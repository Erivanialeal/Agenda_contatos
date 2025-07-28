from flask import Flask
# Ensure that routes.py exists in the same directory as app.py
from app.routes.contatos import contatos_bp
from database.db import Database
#
app = Flask(__name__)
#criar a tabela ao iniciar aplicação
banco= Database()
banco.tabela()
app.register_blueprint(contatos_bp)

if __name__ == "__main__":
    app.run(debug=True)