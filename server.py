from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Servidor HTTP está funcionando!"

if __name__ == '__main__':
    # host='0.0.0.0' permite acesso externo
    # debug=True mostra mensagens de erro detalhadas
    app.run(host='0.0.0.0', port=5000, debug=True)
