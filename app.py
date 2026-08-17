from flask import Flask

app = Flask(__name__)

# Rota Raiz.

@app.route('/')
def welcome():
    return '\
    <h1>Bem vindo!</h1><br>\
    <a href="status">Status</a><br>\
    <a href="tickets">Tickets</a><br>\
    <a href="sobre">Sobre</a>\
    '

# Rota Raiz.

@app.route('/status')
def status():
    return {'servico': 'OpsTrackAPI','status': 'online'}

# Rota Raiz.

@app.route('/tickets')
def tickets():
    return{
    "id": "1",
    "titulo": "Erro 404 ao acessar relatório de vendas",
    "descricao": "Usuário reporta erro pagina não achada e erro HTTP 404 ao tentar exportar o relatório consolidado do mês anterior.",
    "categoria": "3",
    "prioridade": "Alta",
    "status": "Aberto",
    "criado_em": "2026-08-17T08:30:00Z",
    "atualizado_em": "2026-08-17T08:32:00Z",
    "solicitante": {
      "nome": "Ana Silva",
      "email": "ana.silva@empresa.com",
      "departamento": "6"
    },
  }

# Rota Raiz.

@app.route('/sobre')
def sobre():
    return """<h1>Bem vindo! esse é meu projeto API Opstrack!</h1><br>
        <a href="/">Voltar ao portal.</a>
        """



if __name__ == '__main__':
    app.run(debug=True)