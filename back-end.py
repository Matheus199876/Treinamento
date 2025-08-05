# pip install flask flask-cors
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

@app.route("/calcular", methods=["POST"])
def calcular():
    data = request.get_json()

    try:
        num1 = float(data["num1"])
        num2 = float(data["num2"])
        operador = data["operador"]

        if operador == "+":
            resultado = num1 + num2
        elif operador == "-":
            resultado = num1 - num2
        elif operador == "*":
            resultado = num1 * num2
        elif operador == "/":
            if num2 == 0:
                return jsonify({"resultado": "Erro: Divisão por zero"}), 400
            resultado = num1 / num2
        else:
            return jsonify({"resultado": "Erro: Operador inválido"}), 400

        return jsonify({"resultado": f"{resultado}"})
    
    except (ValueError, KeyError):
        return jsonify({"resultado": "Erro: Entrada inválida"}), 400

if __name__ == "__main__":
    app.run(debug=True)

