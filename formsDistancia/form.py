from flask_wtf import Form
from wtforms import FloatField

from wtforms import SelectField, RadioField, StringField
from wtforms.validators import DataRequired


class Inputs(Form):
  color1 = SelectField('color1',choices=['Negro','Cafe','Rojo','Naranja','Amarillo','Verde','Azul','Violeta','Gris','Blanco'])
  color2 = SelectField('color2',choices=['Negro','Cafe','Rojo','Naranja','Amarillo','Verde','Azul','Violeta','Gris','Blanco'])
  color3 = SelectField('color3',choices=['Negro','Cafe','Rojo','Naranja','Amarillo','Verde','Azul','Violeta','Gris','Blanco'])
  tolerancia = RadioField('Tolerancia',choices=['Oro','Plata'], default="Oro")

class InputsForm(Form):
    x1 = FloatField('x1')
    x2 = FloatField('x2')
    y1 = FloatField('y1')
    y2 = FloatField('y2')

class Idiomas(Form):
  ingles = StringField(
     label="Ingles",
     validators=[DataRequired("El campo es requerido")]
  )
  spanish = StringField(
     label="Español",
     validators=[DataRequired("El campo es requerido")]
  )

  q = StringField(
     label="Buscar...",
  )

  idioma  = RadioField('Idioma',choices=['Ingles','Español'], default="Ingles")
    

def saveInFile(espa,ing):
  file = open("templates/dicc.txt", "a")
  file.write(f"\n{espa}:{ing}")


# busqueda el elemento
def searchInFile(q,idioma):
  file =  open("templates/dicc.txt", "r")
   #el formato es: español:ingles
  q_result = ""
  for line in file:
      if q in line:
        q_result = line
        return q_result.split(":")[0] if idioma == "Español" else q_result.split(":")[1]

