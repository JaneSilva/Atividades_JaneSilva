#coding: UTF-8
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def pagina_index():
	return render_template("index.html")

@app.route("/cadastrar/", method=["GET"])
def dados():
	nome = request.args.get("nome")
	email = request.args.get("email")
	telefone = request.args.get("telefone")
	return render_template("cadastro_realizado.html",**localls())	

@app.route("/cadastrar/", method=["POST"])
def dados():
	nome = request.form.get("nome")
	email = request.form.get("email")
	telefone = request.form.get("telefone")
	return render_template("cadastro_realizado.html",**localls())

@app.route("/dados/<nome>/<email>/<telefone>/")
def dados(nome,email,telefone):
	return render_template("dados.html", **locals())