from setting_test import session
from init_tables import Books, Users, Thesis, Lending, Sessions


class Books_Ctrl:
    def __int__(self):
        pass

    def insert(self, isbn, title, place):
        isbn = int(isbn.replace("-", ""))
        book = Books()
        book.isbn = isbn
        book.title = title
        book.place = place
        session.add(book)

        session.flush()
        session.commit()

    def delete(self, id_):
        book = session.query(Books).filter(Books.id == id_).first()
        session.delete(book)
        session.commit()

    def select(self):
        return session.query(Books.id, Books.isbn, Books.title, Books.place).all()[:]

class Users_Ctrl:
    def __int__(self):
        pass
    
    def insert(self, k_number, name):
        user = Users()
        user.k_number = k_number 
        user.name = name 
        session.add(user)  

        session.flush()
        session.commit()

    def delete(self, id_):
        user = session.query(Users).filter(Users.id == id_).first()
        session.delete(user)
        session.commit()

    def select(self):
        return session.query(Users.id, Users.k_number, Users.name).all()[:]

class Lending_Ctrl:
    def __int__(self):
        pass

    def insert(self, user_id, book_id, date):
        lending = Lending()
        lending.user_id = user_id 
        lending.book_id = book_id 
        lending.date = date
        session.add(lending)  

        session.flush()
        session.commit()

    def delete(self, id_):
        lending = session.query(Lending).filter(Lending.id == id_).first()
        session.delete(lending)
        session.commit()

    def select(self):
        return session.query(Lending.id, Lending.user_id, Lending.book_id, Lending.date).all()[:]

class Sessions_Ctrl:
    def __int__(self):
        pass

    def insert(user_id, session_id, expiration_id):
        sessions = Sessions()
        sessions.user_id = user_id 
        sessions.session_id = session_id 
        sessions.expiration_id = expiration_id
        session.add(session)

        session.flush()
        session.commit()

    def delete(self, id_):
        session_ = session.query(Sessions).filter(Sessions.id == id_).first()
        session.delete(session_)
        session.commit()

    def select(self):
        return session.query(Sessions.id, Sessions.user_id, Sessions.session_id, Sessions.expiration_date).all()[:]

class Thesis_Ctrl:
    def __init__(self):
        pass

    def insert(self, thesis_id, title):
        thesis = Thesis()
        thesis.thesis_id = thesis_id
        thesis.title = title
        session.add(thesis)

        session.flush()
        session.commit()

    def delete(self, id_):
        thesis = session.query(Thesis).filter(Thesis.id == id_).first()
        session.delete(thesis)
        session.commit()

    def select(self):
        return session.query(Thesis.id, Thesis.identifier, Thesis.title).all()[:]

if __name__ == "__main__":
    print("DB Control Class．")
