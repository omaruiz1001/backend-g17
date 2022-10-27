from __future__ import division
from flask import Flask,request

app = Flask(__name__)

@app.route('/')
def index():
    return '<center><h1>BIENVENIDO A MI SERVIDOR WEB CON FLASK</h1></center>'

@app.route('/saludo')
def mostrarSaludo():
    nombre = request.args.get('nombre','no hay nombre')
    return '<b>Hola {}</b>'.format(nombre)

@app.route('/suma')
def suma():
    n1=request.args.get('n1','0')
    n2=request.args.get('n2','0')
    resultado=int(n1) + int(n2)
    return 'la suma de {} + {} es {}'.format(n1,n2,resultado)

@app.route('/operaciones')
def operaciones():
    n1=request.args.get('n1','0')
    n2=request.args.get('n2','0')
    operacion=request.args.get('ope','')
    
    if(operacion=="suma"):
        resultado= int(n1) + int(n2)
    elif(operacion=="resta"):
        resultado= int(n1) - int(n2)
    elif(operacion=="multiplicacion"):
        resultado= int(n1) * int(n2)
    elif(operacion=="division"):
        resultado= int(n1) / int(n2)
    else:
        resultado = ''
    if(resultado!=''):
        return 'el resultado de la {} entre {} y {} es {}'.format(operacion,n1,n2,resultado)
    else:
        return 'la operacion no es correcta!!!'

app.run(debug=True)