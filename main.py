from flask import Flask
# Ensure that routes.py exists in the same directory as app.py
from app.routes.contatos import contatos_bp
app = Flask(__name__)
#registrar as rotas
app.register_blueprint(contatos_bp)

if __name__ == "__main__":
    app.run(debug=True, threaded=True)