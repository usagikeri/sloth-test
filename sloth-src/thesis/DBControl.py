from setting_test import session
from init_tables import Books, Users, Thesis, Lending, Sessions


class Thesis_Ctrl:
    def __init__(self):
        pass

    def insert(self, thesis_id, title):
        thesis = Thesis()
        thesis.idetifier = thesis_id
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
