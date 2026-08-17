from flask import Flask

app = Flask(__name__)

# Rota Raiz.

@app.route('/')
def welcome():
    return "<h1>Bem vindo!</h1>"

# Rota Raiz.

@app.route('/status')
def status():
    return {'servico': 'OpsTrackAPI','status': 'online'}

# Rota Raiz.

@app.route('/tickets')
def tickets():
    return {'servico': 'OpsTrackAPI','status': 'online'}

# Rota Raiz.

@app.route('/sobre')
def sobre():
    return {'servico': 'OpsTrackAPI','status': 'online'}



if __name__ == '__main__':
    app.run(debug=True)