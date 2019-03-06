from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class UserSignup(FlaskForm):
    firstname = StringField('Firstname: ', validators=[DataRequired()])
    lastname = StringField('Lastname: ', validators=[DataRequired()])
    username = StringField('Username: ', validators=[DataRequired()])
    email = StringField('Email: ', validators=[DataRequired()])
    cell_number = IntegerField('Cell Number: ', validators=[DataRequired()])
    address = StringField('Address: ', validators=[DataRequired()])
    submit = SubmitField('Create')


class BookRegistration(FlaskForm):
    title = StringField('Title: ', validators=[DataRequired()])
    year = IntegerField('Year: ', validators=[DataRequired()])
    pages = IntegerField('Pages: ', validators=[DataRequired()])
    author = StringField('Author: ', validators=[DataRequired()])
    publisher = StringField('Publisher: ', validators=[DataRequired()])
    submit = SubmitField('Create')



