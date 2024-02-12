Como hacer lo de cardiel

paso 1: Flask-wtf

en otro archivo aparte main vas a crear una clase que use flask-wtf
para hacer un Select y un radio vas a importar SelectField y RadioField
y le agregas las opciones con choices
ejemplo

from wtforms import SelectField, RadioField

banda1 = SelectField('Banda 1', choices=['verde', 'rojo', 'azul'])

paso 2: crear el macro

solo copia y pega el macro que ya usamos

paso 3: main

en el main de python vas a crear un servicio por ejemplo "/calRes" que reciba los datos del formulario y haga el calculo
que permita get y post
con el get solo vas a hacer el render_template del formulario y pasarle el formulario

paso 4: html
usando el macro que ya hicimos vas a crear el formulario
usando el formulario que pasaste en el render_template
ahora cuando hagas el submit del formulario se va a enviar a "/calRes" y vas a recibir los datos en el main de python

pasos 5: hacer el calculo
en el main de python vas a recibir los datos del formulario y hacer el calculo
y vas a retornar el otro render_template con el resultado del calculo

paso 6: html
en el html vas a recibir el resultado del calculo y lo vas a mostrar en una tabla
y dependiendo del color de las bandas vas a mostrar el color de la banda en la tabla
