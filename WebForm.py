from flask import Flask, render_template, redirect, url_for, session
from flask_wtf import Form
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = 'Web Development'


class NameForm(Form):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        print(form.errors)
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'))


app.run(debug=True)

