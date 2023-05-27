from flask_wtf import FlaskForm
from wtforms.fields import StringField,SubmitField
from wtforms.validators import DataRequired

class ProyectoForm(FlaskForm):
    nombre = StringField('Nombre',validators=[DataRequired()])
    descripcion = StringField('Descripción',validators=[DataRequired()])
    imagen = StringField('Imagen',validators=[DataRequired()])
    submit = SubmitField('Guardar')

class RedForm(FlaskForm):
    icono = StringField('Icono',validators=[DataRequired()])
    url = StringField('URL',validators=[DataRequired()])
    submit = SubmitField('Guardar')