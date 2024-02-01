from flask_wtf import Form
from wtforms import FloatField



class InputsForm(Form):
    x1 = FloatField('x1')
    x2 = FloatField('x2')
    y1 = FloatField('y1')
    y2 = FloatField('y2')
    