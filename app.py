from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dados de usuários (geralmente isso seria armazenado em um banco de dados)
usuarios = {'usuario1': 'senha1', 'usuario2': 'senha2'}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('cadastro.html')

@app.route('/users')
def users():
    return render_template('users.html', users = usuarios)

@app.route('/login', methods=['POST'])
def login():
    usuario = request.form['usuario']
    senha = request.form['senha']
    if usuario in usuarios and usuarios[usuario] == senha:
        return render_template('success.html', message = 'Olá ' + usuario + '!')
    else:
        return render_template('fail.html', message = 'Credenciais inválidas. Por favor, tente novamente.')

@app.route('/cadastro', methods=['POST'])
def cadastro():
    novo_usuario = request.form['novousuario']
    nova_senha = request.form['novasenha']
    if novo_usuario not in usuarios:
        usuarios[novo_usuario] = nova_senha
        return render_template('success.html', message = 'Usuário ' + novo_usuario + ' cadastrado com sucesso!')
    else:
        return render_template('fail.html', message = 'Usuário já existe. Por favor, escolha outro nome de usuário.')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)