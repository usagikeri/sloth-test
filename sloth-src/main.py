from setting_env import session
from init_tables import *
import sys

args = sys.argv

def insert(*value):
    if len(value) == 3 and isinstance(value[0], str):
        isbn, title, place = value
        """
        isbnをintに変換する処理が必要
        """
        book = Books()
        book.isbn = isbn 
        book.title = title 
        book.place = place
        session.add(book)  
        session.commit()

    elif len(value) == 3 and isinstance(value[0], int):
        user_id, session_id, expiration_id = value
        sessions = Sessions()
        sessions.user_id = user_id 
        sessions.session_id = session_id 
        sessions.expiration_id = expirarion_id
        session.add(session)
        session.commit()

    elif len(value) == 2 and isinstance(value[0], str):
        k_number, name = value

        user = Users()
        user.k_number = k_number 
        user.name = name 
        session.add(user)  
        session.commit()

    elif len(value) == 2 and isinstance(value[0], int):
        user_id, book_id = value

        lending = Lending()
        lending.user_id = user_id 
        lending.book_id = book_id 
        session.add(lending)  
        session.commit()

    else:
        print('Error:Invalid argument')
        sys.exit()

if 1 < len(args):
    insert(*args)

print('--------------------')
print(session.query(Books.id, Books.isbn, Books.title, Books.place).all()[:])
print('--------------------')
print(session.query(Users.id, Users.k_number, Users.name).all()[:])
print('--------------------')
print(session.query(Lending.id, Lending.user_id, Lending.book_id).all()[:])
