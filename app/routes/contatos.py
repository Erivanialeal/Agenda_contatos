from shared.imports import  Blueprint, render_template,sqlite3,request,jsonify,redirect,url_for

# Criando o Blueprint para os contatos
contatos_bp= Blueprint('contatos', __name__)

#rota para listar contatos
@contatos_bp.route('/')
def lista_de_contatos():
    #conectar ao banco
    conec=sqlite3.connect('meu_banco.db')
    cursor=conec.cursor()
    #seleciona a tabela
    cursor.execute('SELECT id,nome,telefone,email from agenda LIMIT 50')
    # busca todos os resultados
    contatos= cursor.fetchall()
    print(contatos)
    conec.close()
    #retorna o templante
    return render_template('index.html',contatos=contatos)

#rota para adicionar contato
@contatos_bp.route('/contatos/adicionar',methods=['POST'])
def adicionar_contato():
    data= request.get_json()
    # Se não houver dados ou se o JSON for inválido, retorna um erro
    if not data:
        return jsonify({"erro": "JSON inválido ou não enviado."}), 400
    
    nome=data.get("nome")
    telefone=data.get('telefone')
    email=data.get('email')

    if not nome:
        return jsonify({"erro:","O campo nome não pode está vazio."}), 400
    
    try:
        #conectar ao banco
        conec=sqlite3.connect('meu_banco.db')
        cursor=conec.cursor()
        #inserir no banco de dados
        cursor.execute('INSERT INTO agenda (nome,telefone,email) VALUES (?,?,?)',(nome,telefone,email))
        #commitar as alterações
        conec.commit()
        return jsonify({'mensagem':'Contato adicionado com sucesso!'}),200
    except Exception as e:
        return jsonify({"erro":f"Erro ao adicionar contato {e}"}),500
    finally:
        conec.close()
    

# rota para excluir um contato na agenda.
@contatos_bp.route('/contatos/excluir', methods=['DELETE'])
def excluir_contato():
    #receber os dados necessarios
    data= request.get_json()
    if not data:
        return({"erro","Json invalido"}),400
    try:
        #definir a variavel id
        contato_id=data.get('id')
        if not contato_id:
            return jsonify({'erro':'Id do contato é obrigatório'})
        contato_id=int(contato_id)
    except ValueError:
        return({"erro":"ID invalido"}),400
    try:
        # conectar ao banco
        conn=sqlite3.connect('meu_banco.db')
        cursor=conn.cursor()
        # buscar o contato no banco
        cursor.execute('SELECT * FROM agenda WHERE id= ?',(contato_id,))
        #armazenar o fechone
        resultado=cursor.fetchone()
        # se não encontar,retornar erro
        if resultado is None:
            return jsonify({'erro': "contato não encontrado"}),404
        # se encontrar deletar contato
        cursor.execute('DELETE  FROM agenda WHERE id = ?',(contato_id,))
        #commitar as alterações
        conn.commit()
        # retornar mensagem de sucesso.
        return ({"mensagem":f"Contato {contato_id} deletado com sucesso"}),200
    # fechar o commit no (finnaly)
    except Exception as e:
        return jsonify({f"erro":f"Erro ao deletar: {e}"}),500
    finally:
        conn.close()

# rota para buscar contato
@contatos_bp.route("/contatos/pesquisar",methods=["GET"])
def pesquisar_contato():
    #pegar o paramentro nome
    nome = request.args.get("nome")
    if not nome:
        return redirect(url_for('contatos_bp.lista_de_contatos'))
    #conectar ao banco
    conn=sqlite3.connect("meu_banco.db")
    cursor=conn.cursor()
    #buscar o contato no banco
    cursor.execute('SELECT id, nome, telefone, email from agenda WHERE nome= ?',(nome))
    # armazenar o fechone
    resultado= cursor.fetchone()
    #tratar erros
    if resultado is None:
        return jsonify({"erro"," contato não encontrado"}), 404
    return render_template("index.html",contatos=resultado)




