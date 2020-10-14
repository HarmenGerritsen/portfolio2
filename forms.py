from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    fname = StringField('Voornaam', render_kw={"placeholder": 'Je voornaam..'}, validators=[DataRequired()])
    lname = StringField('Achternaam', render_kw={"placeholder": 'Je achternaam..'}, validators=[DataRequired()])
    email = StringField('Email', render_kw={"placeholder": 'Je email..'}, validators=[DataRequired(), Email()])
    message = TextAreaField('Bericht', render_kw={"placeholder": 'Je bericht..','cols': 30, 'rows': 10},
                            validators=[DataRequired()])
    submit = SubmitField('Verstuur bericht')