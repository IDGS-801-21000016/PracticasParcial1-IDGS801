from flask_wtf import Form
from wtforms import SelectField, RadioField


class InputsForm(Form):
  color1 = SelectField('color1',choices=['Negro','Cafe','Rojo','Naranja','Amarillo','Verde','Azul','Violeta','Gris','Blanco'])
  color2 = SelectField('color2',choices=['Negro','Cafe','Rojo','Naranja','Amarillo','Verde','Azul','Violeta','Gris','Blanco'])
  color3 = SelectField('color3',choices=['Negro','Cafe','Rojo','Naranja','Amarillo','Verde','Azul','Violeta','Gris','Blanco'])
  tolerancia = RadioField('Tolerancia',choices=['Oro','Plata'], default="Oro")