# from sql_alchemy import Role, User
from LibraryManagementSystem import User

user = User.query.filter_by(username='shakirmahmood').first()
print(user.username)


# user = User.query.filter_by(username='Shakir').first()
# print(user)
#
# user_role = Role.query.filter_by(name='Administrator').first()
# print(user_role)
#
#
# print(user_role.users.order_by(User.username).all())
#
# print(user_role.users.count())