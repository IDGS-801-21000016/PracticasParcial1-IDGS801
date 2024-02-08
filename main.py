from flask import Flask, request, render_template
import math
from formsDistancia.form import InputsForm, Inputs as Ip

app = Flask(__name__)


@app.route('/')
def operasBas():
  	return render_template('operasBas.html')

@app.route('/resistencia',  methods=['GET', 'POST'])
def resistencia():
    form = Ip(request.form)
    color1 = None
    color2 = None
    color3 = None
    tolerancia = None
    isRegistered = {
        color1:0
    }
    #['Negro','Cafe','Rojo','Naranja','Amarillo','Verde','Azul','Violeta','Gris','Blanco']
    tableRegistecia = {
        'Negro':'0',
        'Cafe': '1',
        'Rojo':'2',
        'Naranja':'3',
        'Amarillo':'4',
        'Verde':'5',
        'Azul':'6',
        'Violeta':'7',
        'Gris':'8',
        'Blanco':'9'
    }

    tole = {
        'Oro':5,
        'Plata':10
    }

    bandaMulti ={
        'Negro':1,
        'Cafe': 10,
        'Rojo':100,
        'Naranja':1000,
        'Amarillo':10000,
        'Verde':100000,
        'Azul':1000000,
        'Violeta':10000000,
        'Gris':100000000,
        'Blanco':1000000000
    }

    color={
        'Negro':'style:"background-color:black;"',
        'Cafe': 'style:"background-color:brown;"',
        'Rojo':'style:"background-color:red;"',
        'Naranja':'style:"background-color:orange;"',
        'Amarillo':'style:"background-color:yellow;"',
        'Verde':'style:"background-color:green;"',
        'Azul':'style:"background-color:blue;"',
        'Violeta':'style:"background-color:violet;"',
        'Gris':'style:"background-color:gray;"',
        'Blanco':'style:"background-color:white;"'
    }

    if request.method == 'POST':
        color1 = request.form['color1']
        color2 = request.form['color2']
        color3 = request.form['color3']
        tolerancia = request.form['tolerancia']

        c1 =color[color1]
        c2= color[color2]
        c3 = color[color3]
        
        v1 = int(tableRegistecia[color1])
        v2 = int(tableRegistecia[color2])
        band = int(bandaMulti[color3])
        tolerancia = tole[tolerancia]

        valor =int(f"{v1}{v2}")* band

        if tolerancia == 5:
            tole = 'Dorado 5%'
        else:
            tole = 'Plateado 10%'
                
        valorMinimo = valor - (valor * tolerancia/100)
        valorMaximo = valor + (valor * tolerancia/100)


        return render_template('registencia.html', form=form, color1=color1,color2=color2, color3=color3, valor=valor, valorMaximo=valorMaximo, valorMinimo=valorMinimo,tole=tole,c1=c1,c2=c2,c3=c3)

    return render_template('registencia.html', form=form)


@app.route('/distancia', methods=['GET', 'POST'])
def distancia():
    form = InputsForm(request.form)
    x1 = None
    x2 = None
    y1 = None
    y2 = None
    distancia = None
    if request.method == 'POST':
      x1 = form.x1.data
      x2 = form.x2.data
      y1 = form.y1.data
      y2 = form.y2.data
      distancia = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return render_template('distancia.html', form=form,distancia=distancia)

@app.route('/resultado' , methods=['GET', 'POST'])
def resultado():
    if request.method == 'POST':
        n1 = int(request.form['n1'])
        n2 = int(request.form['n2'])
        tipo = request.form['tipo']

        if tipo == 'suma':
            resultado = n1 + n2
            return f"La suma de {n1} y {n2} es {resultado}"
        elif tipo == 'resta':
            resultado = n1 - n2
            return f"La resta de {n1} y {n2} es {resultado}"
        elif tipo == 'multiplicacion':
            resultado = n1 * n2
            return f"La multiplicacion de {n1} y {n2} es {resultado}"
        elif tipo == 'division':
            resultado = n1 / n2
            return f"La division de {n1} y {n2} es {resultado}"
        else:
            return "Error"
      
if __name__ == '__main__':
    app.run(debug=True)