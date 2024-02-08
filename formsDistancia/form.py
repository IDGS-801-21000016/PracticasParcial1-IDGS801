from flask_wtf import Form
from wtforms import FloatField

from wtforms import SelectField, RadioField


x =2
y = 3

valor = 'Pu' if x > y else 'to'

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
    