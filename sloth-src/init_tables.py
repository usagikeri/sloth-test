from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime
from setting_test import Base
from setting_test import ENGINE
from sqlalchemy.dialects import mysql
import sys

class Users(Base):
    __tablename__ = 'Users' 
    id = Column('id', Integer, primary_key = True, autoincrement=True)
    k_number = Column('k_number', String(7), nullable=False)
    name = Column('name', String(30), nullable=False)

class Books(Base):
    __tablename__ = 'Books' 
    id = Column('id', Integer, primary_key = True, autoincrement=True)
    isbn = Column('isbn', mysql.BIGINT, nullable=False)
    title = Column('title', String(100), nullable=False)
    place = Column('place', String(1), nullable=False)

class Thesis(Base):
    __tablename__ = 'Thesis'
    id = Column('id', Integer, primary_key = True, autoincrement=True)
    thesis_id = Column('thesis_id', String(64), nullable=False)
    title = Column('title', String(150), nullable=False)

class Lending(Base):
    __tablename__ = 'Lending' 
    id = Column('id', Integer, primary_key = True, autoincrement=True)
    user_id = Column('user_id', Integer,  \
	ForeignKey('Users.id',onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    book_id = Column('book_id', Integer,  \
	ForeignKey('Books.id',onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    date = Column('date', Date, nullable=False)
	
    user_id_relation = relationship('Users')
    book_id_relation = relationship('Books')

class Sessions(Base):
    __tablename__ = 'Sessions'
    id = Column('id', Integer, primary_key = True, autoincrement=True)
    user_id = Column('user_id', Integer,  \
	ForeignKey('Users.id',onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    session_id = Column('session_id', String(64), nullable=False)
    expiration_date = Column('expiration_date', Date, nullable=False) 

    user_id_relation = relationship('Users')


def main(args):
    if len(args) > 1 and args[1] == 'create':
        # テーブル作成
        Base.metadata.create_all(bind=ENGINE)
    elif len(args) > 1 and args[1] == 'drop':
        # テーブル削除
        Base.metadata.drop_all(bind=ENGINE)
    else:
        print('''Error:Invalid argument
              create:create tables
              drop:delete tabels''')
        sys.exit()

if __name__ == "__main__":
    main(sys.argv)
