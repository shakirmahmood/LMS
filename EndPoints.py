from LibraryManagementSystem import User, Book, Acquire, app, db
from flask import request, Response
import json

db.init_app(app)
db.create_all()


def display_data(user=None, book=None):
    if user:
        data = {'firstname': user.firstname,
                'lastname': user.lastname,
                'username': user.username,
                'email': user.email,
                'cell_number': user.cell_number,
                'address': user.address
                }
        return data

    elif book:
        data = {'title': book.title,
                'year': book.year,
                'pages': book.pages,
                'author': book.author,
                'publisher': book.publisher
                }
        return data
    return create_response('Data not found')


def response(users=None, books=None):
    if users:
        data = []
        for user in users:
            data.append(display_data(user=user))

    elif books:
        data = []
        for book in books:
            data.append(display_data(book=book))
        print(data)
    return Response(json.dumps(data, indent=4), mimetype='application/json')


def create_response(data):
    return Response(json.dumps(data, indent=4), mimetype='application/json')


def create(UserOrBook):
    data = request.get_json()
    if UserOrBook == 'user':
        username = User.query.filter_by(username=data['username']).first()
        email = User.query.filter_by(email=data['email']).first()

        if username is None and email is None:
            user = User(firstname=data['firstname'],
                        lastname=data['lastname'],
                        username=data['username'],
                        email=data['email'],
                        cell_number=data['cell_number'],
                        address=data['address'])
            db.session.add(user)
            db.session.commit()
            return create_response("User Created")
        else:
            return create_response("User Already Exists")

    if UserOrBook == 'book':
        book = Book(title=data['title'],
                    year=data['year'],
                    pages=data['pages'],
                    author=data['author'],
                    publisher=data['publisher'])
        db.session.add(book)
        db.session.commit()
        return create_response("Book Created")


def search(UserOrBook):
    if UserOrBook == 'user':
        if request.args.get('all'):
            users = User.query.all()
            return response(users=users)

        if request.args.get('firstname'):
            users = User.query.filter_by(firstname=request.args.get('firstname')).all()
            return response(users=users)

        if request.args.get('lastname'):
            users = User.query.filter_by(lastname=request.args.get('lastname')).all()
            return response(users=users)

        if request.args.get('username'):
            users = User.query.filter_by(username=request.args.get('username')).all()
            return response(users=users)

        if request.args.get('email'):
            users = User.query.filter_by(email=request.args.get('email')).all()
            return response(users=users)

        if request.args.get('cell_number'):
            users = User.query.filter_by(cell_number=request.args.get('cell_number')).all()
            return response(users=users)

        if request.args.get('address'):
            users = User.query.filter_by(address=request.args.get('address')).all()
            return response(users=users)

    if UserOrBook == 'book':
        if request.args.get('all'):
            books = Book.query.all()
            return response(books=books)

        if request.args.get('title'):
            books = Book.query.filter_by(title=request.args.get('title')).all()
            print('yes')
            return response(books=books)

        if request.args.get('year'):
            books = Book.query.filter_by(year=request.args.get('year')).all()
            return response(books=books)

        if request.args.get('pages'):
            books = Book.query.filter_by(pages=request.args.get('pages')).all()
            return response(books=books)

        if request.args.get('author'):
            books = Book.query.filter_by(author=request.args.get('author')).all()
            return response(books=books)

        if request.args.get('publisher'):
            books = Book.query.filter_by(publisher=request.args.get('publisher')).all()
            return response(books=books)


def update_data(UserOrBook):
    if UserOrBook == 'book':
        if request.args.get('title'):
            update = Book.query.filter_by(title=request.args.get('title')).first()
            update.title = request.args.get('update')
            db.session.commit()
            return create_response(display_data(book=update))

        if request.args.get('year'):
            update = Book.query.filter_by(year=request.args.get('year')).first()
            update.year = request.args.get('update')
            db.session.commit()
            return create_response(display_data(book=update))

        if request.args.get('pages'):
            update = Book.query.filter_by(pages=request.args.get('pages')).first()
            update.pages = request.args.get('update')
            db.session.commit()
            return create_response(display_data(book=update))

        if request.args.get('author'):
            update = Book.query.filter_by(author=request.args.get('author')).first()
            update.author = request.args.get('update')
            db.session.commit()
            return create_response(display_data(book=update))

        if request.args.get('publisher'):
            update = Book.query.filter_by(publisher=request.args.get('publisher')).first()
            update.publisher = request.args.get('update')
            db.session.commit()
            return create_response(display_data(book=update))

    if UserOrBook == 'user':
        if request.args.get('firstname'):
            update = User.query.filter_by(firstname=request.args.get('firstname')).first()
            update.firstname = request.args.get('update')
            db.session.commit()
            return create_response(display_data(user=update))

        if request.args.get('lastname'):
            update = User.query.filter_by(lastname=request.args.get('lastname')).first()
            update.lastname = request.args.get('update')
            # if update is None:
            #     db.session.add()
            db.session.commit()
            return create_response(display_data(user=update))

        if request.args.get('username'):
            update = User.query.filter_by(username=request.args.get('username')).first()
            update.username = request.args.get('update')
            db.session.commit()
            return create_response(display_data(user=update))

        if request.args.get('email'):
            update = User.query.filter_by(email=request.args.get('email')).first()
            update.email = request.args.get('update')
            db.session.commit()
            return create_response(display_data(user=update))

        if request.args.get('cell_number'):
            update = User.query.filter_by(cell_number=request.args.get('cell_number')).first()
            update.cell_number = request.args.get('update')
            db.session.commit()
            return create_response(display_data(user=update))

        if request.args.get('address'):
            update = User.query.filter_by(address=request.args.get('address')).first()
            update.address = request.args.get('update')
            db.session.commit()
            return create_response(display_data(user=update))


def delete(UserOrBook):
    if UserOrBook == 'user':
        if request.args.get('username'):
            user = User.query.filter_by(username=request.args.get('username')).first()
            db.session.delete(user)
            db.session.commit()
            return create_response('User is deleted')
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
            db.session.delete(user)
            db.session.commit()
            return create_response('User is deleted')

    if UserOrBook == 'book':
        if request.args.get('title'):
            book = Book.query.filter_by(title=request.args.get('title')).first()
            db.session.delete(book)
            db.session.commit()
            return create_response('Book is deleted')

        if request.args.get('author'):
            book = Book.query.filter_by(author=request.args.get('author')).first()
            db.session.delete(book)
            db.session.commit()
            return create_response('Book is deleted')

        if request.args.get('publisher'):
            book = Book.query.filter_by(Publisher=request.args.get('publisher')).first()
            db.session.delete(book)
            db.session.commit()
            return create_response('Book is deleted')


@app.route('/<UserOrBook>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def home(UserOrBook):
    if request.method == 'POST':
        return create(UserOrBook)

    elif request.method == 'GET':
        return search(UserOrBook)

    elif request.method == 'PUT':
        return update_data(UserOrBook)

    elif request.method == 'DELETE':
        return delete(UserOrBook)


@app.route('/acquire/<username>/<booktitle>', methods=['POST', 'DELETE'])
def acquire_book(username, booktitle):
    if request.method == 'POST':
        user = User.query.filter_by(username=username).first()
        book = Book.query.filter_by(title=booktitle).first()

        if book is None or user is None:
            return create_response("Sorry! The book/user is not present")

        acquired = Acquire(booktitle=book.title,
                           bookyear=book.year,
                           bookpages=book.pages,
                           bookauthor=book.author,
                           bookpublisher=book.publisher,
                           user=user.username)
        db.session.add(acquired)

        book = Book.query.filter_by(title=booktitle).first()
        db.session.delete(book)

        db.session.commit()
        return create_response("Book Acquired")

    elif request.method == 'DELETE':
        acquired = Acquire.query.filter_by(booktitle=booktitle).first()
        if acquired is None:
            return create_response("Book is not acquired")
        temp_book = Book(title=acquired.booktitle,
                         year=acquired.bookyear,
                         pages=acquired.bookpages,
                         author=acquired.bookauthor,
                         publisher=acquired.bookpublisher)
        db.session.delete(acquired)
        db.session.add(temp_book)
        db.session.commit()

    return create_response("Book Returned")


if __name__ == '__main__':
    app.run(debug=True)



