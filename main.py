from flask import Flask ,request,redirect,flash,url_for
from flask import render_template
from graficos import *
from request import *
import requests
from flask import redirect


app = Flask(__name__)

user_loged = False
app.secret_key = 'my_secret_key'


@app.route('/', methods = ['POST','GET'])
def home (name=None):
  
    return render_template('trades.html')
    

@app.route("/home")
def hello(name=None):
    grafico_area  = generar_grafico_area()
    grafico_pie = generar_grafico_pie()
    long_bar_chart = generate_long_bar_chart()
    dif_bar_chart= generate_dif_bar_chart()
    return render_template('index.html', graph=grafico_area,
                            graph1=generar_grafico_area(),
                            graph2=generar_grafico_area(),
                            graph3=grafico_pie,
                            graph4=long_bar_chart,
                            graph5=dif_bar_chart)



@app.route('/registro')
def registro_vista():
     return render_template('registro.html')

@app.route('/login')
def login_vista():
     return render_template('login.html')

@app.route('/registro', methods=['POST'])
def registro_usuario():
    try:
        respuesta = registrar_usuario(request, requests)
        print (respuesta)

    except Exception as e:
        mensaje = 'Error al registrar usuario: {e}'
        print(f'Error al registrar usuario: {e}')
    else:
        mensaje = 'Usuario creado correctamente '
        print('Usuario creado exitosamente.')
    
    return redirect('/', mensaje= mensaje ) 

@app.route('/registro_cuenta', methods=['POST'])
def registro_cuenta():
    try:
        respuesta = registrar_cuenta_nueva(request, requests)
        print (respuesta)
    except Exception as e:
        print(f'Error al registrar cuenta: {e}')
        respuesta = None
    else:
        print('Cuenta creada exitosamente.')
    return redirect('/')

@app.route('/registro_trade', methods=['POST'])
def registro_trade():
    mensaje = 'onnti'
    email = request.form['Email']
    trade_data = {key: request.form[key] for key in request.form if key != 'Email' }
    trade_data['Estado'] = '1'
    url = f'http://127.0.0.1:8000/trades/crear/?email={email}'
    response = requests.post(url=url, json=trade_data)
    try:
        response.raise_for_status()
    except Exception as e:
        mensaje = f'Error al registrar el Trade: {e.response.json()["detail"]}'

        print(f'Error al registrar el Trade: {e.response.json()["detail"]}')
    else:
        mensaje = 'Trade creado exitosamente.'
        print('Trade creado exitosamente.')
    
    return render_template('trades.html' , mensaje = mensaje)
