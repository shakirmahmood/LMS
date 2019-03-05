from flask import Flask, render_template, redirect, url_for, session
from flask_wtf import Form
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired
from sql_alchemy import db, Role, User, app


# app = Flask(__name__)
# app.secret_key = 'Web Development'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# db.init_app(app)


class NameForm(Form):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        print(user)
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['known'] = False
        else:
            session['known'] = True
            session['name'] = form.name.data
            form.name.data = ''
            return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'), known=session.get('known', False))


if __name__ == '__main__':
    app.run(debug=True)



