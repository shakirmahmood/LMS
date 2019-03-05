from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = 'Web Development'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.sqlite'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username

if __name__ == '__main__':
    # ***********Creating Tables***********
    db.create_all()

    # ***********Deleting Tables***********
    # db.drop_all()

    # ***********Inserting Rows***********
    admin_role = Role(name='admin')
    mod_role = Role(name='Moderator')
    user_role = Role(name='User')
    user_Shakir = User(username='Shakir', role=admin_role)
    user_Shahid = User(username='Shahid', role=user_role)
    user_Nomi = User(username='Nomi', role=user_role)

    print(admin_role.id)

    # db.session.add(admin_role)
    # db.session.add(mod_role)
    # db.session.add(user_role)
    # db.session.add(user_Nomi)
    # db.session.add(user_Shahid)
    # db.session.add(user_Shakir)

    # Preparing to write changes to database
    db.session.add_all([admin_role, mod_role, user_role, user_Shakir, user_Shahid, user_Nomi])

    # Writing changes to database
    db.session.commit()

    print(admin_role.id, mod_role.id, user_role.id)

    # ***********Modifying Rows***********
    admin_role.name = 'Administrator'
    db.session.add(admin_role)
    db.session.commit()

    # ***********Deleting Rows***********
    db.session.delete(mod_role)
    db.session.commit()


    # ***********Querying Rows***********
    print(Role.query.all())
    print(User.query.all())

    # ***********Specific Database Search***********
    print(User.query.filter_by(role=user_role).all())
    print(str(User.query.filter_by(role=user_role).all()))


