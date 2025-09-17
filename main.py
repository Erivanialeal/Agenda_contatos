from flask import Flask
import time
# Ensure that routes.py exists in the same directory as app.py
from app.routes.contatos import contatos_bp
start = time.time() #marca o inicio
app = Flask(__name__)

# medir tempo até aqui
print("Flask inicializado em",time.time() - start,"segundos")
#registrar as rotas
app.register_blueprint(contatos_bp,)

#registrar rotas
print("Blueprint registrada em:",time.time() - start, "segundos")

if __name__ == "__main__":
    print("Iniciando servidor Flask...")
    app.run(debug=False, threaded=True)