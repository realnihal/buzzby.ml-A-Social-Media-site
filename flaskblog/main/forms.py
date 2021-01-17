from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class WeatherForm(FlaskForm):
    CITY = StringField('CITY', validators=[DataRequired()])
    submit = SubmitField('View')