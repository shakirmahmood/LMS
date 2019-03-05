from LibraryManagementSystem import User, db

user = User.query.filter_by(username='shakirmahmood').first()
print(user)
