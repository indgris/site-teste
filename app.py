from flask import Flask

app = Flask(__name__)

@app.rout.("/")
def hello_world():
  return "Olá, mundo! Esse é meu site. (Ingrid Ruela)"
