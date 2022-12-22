from flask import Flask, render_template, request, redirect, session, flash, url_for

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome=nome
        self.categoria=categoria
        self.console=console

jogo1 = Jogo('tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('Mario', 'Plataforma', 'Nintendo')
jogo3 = Jogo('Crash', 'Aventura', 'Playstation')
lista = [jogo1, jogo2, jogo3]

class Usuario:
    def __init__(self, nome, user, senha):
        self.nome = nome
        self.user = user
        self.senha = senha

usuario1 = Usuario("Bruno", "bruno007", "123456")
usuario2 = Usuario("Leo", "leo123", "123456")
usuario3 = Usuario("Victor", "victor09", "123456")

usuarios = { usuario1.user : usuario1,
             usuario2.user : usuario2,
             usuario3.user : usuario3 }

app = Flask(__name__)
app.secret_key = 'admin'

@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect(url_for('index'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.user
            flash(usuario.user + 'logado com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else:
        flash('Usuario não logado!')
        return redirect(url_for('login'))
@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('index'))

app.run(debug=True)