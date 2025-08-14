# A very simple Flask Hello World app for you to get started with...
from flask import Flask
from flask import request
from flask import redirect
from flask import abort

app = Flask(__name__)
@app.route('/')
def hello_world():
    # return '<p>Alterações por meio do GitHub</p><table><tr><td><b>Professor:</b></td><td>Professor Fabio Teixeira</td></tr><tr><td><b>Prontuário:</b></td><td>PT23820X</td></tr></table>'
    return '<h1>Hello World!</h1> <h2>Disciplina PTBDSWS</h2>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)

@app.route('/contextorequisicao')
def req():
    cont_req = request.headers.get('User-Agent') # informação que o servidor pega para saber do navegador e so
    return cont_req

@app.route('/codigostatusdiferente')
def status():
    return '<p>Bad request</p>'

@app.route('/objetoresposta')
def obj():
    return '<h1>This document carries a cookie!</h1>'

@app.route('/redirecionamento')
def redirecionar():
    return redirect('https://ptb.ifsp.edu.br/')

@app.route('/abortar')
def abortar():
    return abort(400)