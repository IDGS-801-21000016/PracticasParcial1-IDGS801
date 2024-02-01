from flask import Flask, request, render_template
import math
from formsDistancia.form import InputsForm

app = Flask(__name__)


@app.route('/')
def operasBas():
  	return render_template('operasBas.html')

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