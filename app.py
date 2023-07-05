from flask import Flask, jsonify, request

app = Flask(__name__)


postagens = [
    {
        'titulo': 'O homem das cavernas',
        'autor': 'Vitor'
    }
    , {
        'titulo': 'Foi descoberto a cura do COVID',
        'autor': 'Vitor'
    }
]

#Rota padrão
@app.route('/api')
def obter_postagens():
    return jsonify(postagens)

#Buscar postagem por id
@app.route('/api/<int:id>', methods=['GET'])
def obter_postagem_por_id(id):
    if postagens[id:]:
        return jsonify(postagens[id], 200)
    else:
        return jsonify({"erro": "Postagem não encontrada"})
    
@app.route('/api', methods=['POST'])
def nova_postagem():
    postagem = request.get_json()
    postagens.append(postagem)
    
    return jsonify(postagem, 200)

@app.route('/api/<int:id>', methods=['PUT'])
def atualizar_postagem(id):
    postagem_atualizada = request.get_json()
    postagens[id].update(postagem_atualizada)

    return jsonify(postagens[id], 200)

if __name__ == "__main__":
    app.run(debug=True)