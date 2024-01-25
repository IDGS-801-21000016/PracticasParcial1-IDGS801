from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def operasBas():
  	return render_template('operasBas.html')

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