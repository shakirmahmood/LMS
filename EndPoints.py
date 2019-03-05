from LibraryManagementSystem import User, Book, Acquire, app, db
from flask import render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired
import json

db.init_app(app)
db.create_all()


class UserSignup(FlaskForm):
    firstname = StringField('Firstname: ', validators=[DataRequired()])
    lastname = StringField('Lastname: ', validators=[DataRequired()])
    username = StringField('Username: ', validators=[DataRequired()])
    email = StringField('Email: ', validators=[DataRequired()])
    cell_number = IntegerField('Cell Number: ', validators=[DataRequired()])
    address = StringField('Address: ', validators=[DataRequired()])
    submit = SubmitField('Create')


@app.route('/')
def home():
    return json.dumps('{Library Management System: Online}')


@app.route('/register', methods=['GET', 'POST'])
def create():
    newuser = UserSignup(request.form)
    if request.method == "POST":
        username = User.query.filter_by(username=newuser.username.data).first()
        email = User.query.filter_by(email=newuser.email.data).first()

        if username is None and email is None:
            user = User(firstname=newuser.firstname.data,
                        lastname=newuser.lastname.data,
                        username=newuser.username.data,
                        email=newuser.email.data,
                        cell_number=newuser.cell_number.data,
                        address=newuser.address.data)
            db.session.add(user)
            db.session.commit()
            return "<h1>User Created!</h1>"
        else:
            return render_template('create.html', newuser=newuser, warning="User Already Exists")
    return render_template('create.html', newuser=newuser, warning="Hello Stranger!")


def display_data(user):
    if user:
        data = {'Firstname': user.firstname,
                'Lastname': user.lastname,
                'Username': user.username,
                'Email': user.email,
                'Cell Number': user.cell_number,
                'Address': user.address
                }
        return json.dumps(data)
    return json.dumps({'Data': 'Not found'})


@app.route('/search')
def read():
    if request.args.get('firstname'):
        user = User.query.filter_by(firstname=request.args.get('firstname')).first()
        return str(display_data(user))

    if request.args.get('lastname'):
        user = User.query.filter_by(lastname=request.args.get('lastname')).first()
        return str(display_data(user))

    if request.args.get('username'):
        user = User.query.filter_by(username=request.args.get('username')).first()
        return str(display_data(user))

    if request.args.get('email'):
        user = User.query.filter_by(email=request.args.get('email')).first()
        return str(display_data(user))

    if request.args.get('cell_number'):
        user = User.query.filter_by(cell_number=request.args.get('cell_number')).first()
        return str(display_data(user))

    if request.args.get('address'):
        user = User.query.filter_by(address=request.args.get('address')).first()
        return str(display_data(user))


@app.route('/update')
def update():
    if request.args.get('firstname'):
        update = User.query.filter_by(firstname=request.args.get('firstname')).first()
        update.firstname = request.args.get('update')
        db.session.commit()
        return str(display_data(update))

    if request.args.get('lastname'):
        print(request.args.get('lastname'))
        update = User.query.filter_by(lastname=request.args.get('lastname')).first()
        print(update)
        update.lastname = request.args.get('update')
        # if update is None:
        #     db.session.add()
        db.session.commit()
        return str(display_data(update))

    if request.args.get('username'):
        update = User.query.filter_by(username=request.args.get('username')).first()
        update.username = request.args.get('update')
        db.session.commit()
        return str(display_data(update))

    if request.args.get('email'):
        update = User.query.filter_by(email=request.args.get('email')).first()
        update.email = request.args.get('update')
        db.session.commit()
        return str(display_data(update))

    if request.args.get('cell_number'):
        update = User.query.filter_by(cell_number=request.args.get('cell_number')).first()
        print(update.cell_number)
        update.cell_number = request.args.get('update')
        print(update.cell_number)
        db.session.commit()
        return str(display_data(update))

    if request.args.get('address'):
        update = User.query.filter_by(address=request.args.get('address')).first()
        update.address = request.args.get('update')
        db.session.commit()
        return str(display_data(update))


@app.route('/delete')
def delete():
    if request.args.get('username'):
        user = User.query.filter_by(username=request.args.get('username')).first()
        db.session.delete(user)
        db.session.commit()
        return json.dumps('User is deleted')
        # else:
            # print("delete")
            # if str(request.args.get('delete')) == 'firstname':
            #     print("delete")
            #     db.session.delete(user.firstname)
            #     print("delete")
            # elif str(request.args.get('delete')) == 'lastname':
            #     db.session.delete(user.lastname)
            # elif str(request.args.get('delete')) == 'username':
            #     db.session.delete(user.username)
            # elif str(request.args.get('delete')) == 'email':
            #     db.session.delete(user.email)
            # elif str(request.args.get('delete')) == 'cell_number':
            #     db.session.delete(user.cell_number)
            # elif str(request.args.get('delete')) == 'address':
            #     db.session.delete(user.address)
            # db.session.commit()
            # return json.dumps(request.args.get('delete') + " is deleted")

    if request.args.get('email'):
        user = User.query.filter_by(username=request.args.get('email')).first()
        print(user.firstname)
        db.session.delete(user)
        db.session.commit()
        return json.dumps('User is deleted')


if __name__ == '__main__':
    app.run(debug=True)



