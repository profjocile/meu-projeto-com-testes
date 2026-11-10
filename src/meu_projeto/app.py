# app.py
from flask import Flask, jsonify, request


def create_app():
    app = Flask(__name__)
    app.config['TESTING'] = True  # Ativa o modo de teste (melhora logs de erro)
 
    @app.route('/api/saudacao', methods=['GET'])
    def saudacao():
        return jsonify({"mensagem": "Olá, Mundo!"})
 
    @app.route('/api/soma', methods=['POST'])
    def soma():
        dados = request.get_json(silent=True)
        if not isinstance(dados, dict):
            return jsonify({"erro": "O corpo deve ser um objeto JSON."}), 400

        a = dados.get('a')
        b = dados.get('b')
        if any(isinstance(valor, bool) or not isinstance(valor, (int, float)) for valor in (a, b)):
            return jsonify({"erro": "Os campos 'a' e 'b' devem ser números."}), 400

        resultado = a + b
        return jsonify({"resultado": resultado})
 
    return app
 
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)