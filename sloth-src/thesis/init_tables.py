from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime
from setting_test import Base
from setting_test import ENGINE
from sqlalchemy.dialects import mysql
import sys

class Thesis(Base):
    __tablename__ = 'Thesis'
    id = Column('id', Integer, primary_key = True, autoincrement=True)
    thesis_id = Column('thesis_id', String(64), nullable=False)
    title = Column('title', String(150), nullable=False)


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
