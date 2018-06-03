#coding: utf-8
from flask import Flask, render_template

app =  Flask(__name__)

@app.route ("/")
def pagina_index ():
	return render_template("index.html")
	
	
@app.route("/clientes/")
def pagina_clientes():
	return render_template("clientes.html")	
	
@app.route("/produtos/")
def pagina_produtos():
	return render_template("produtos.html")
		
