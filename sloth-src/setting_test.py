from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base

db_config = {'user_name':'sloth',
	     'password':'sloth',
	     'host':'database',
	     'port':'3306',
	     'db_name':'test'}

# mysqlのDBの設定
DATABASE = 'mysql://{0}:{1}@{2}:{3}/{4}?charset=utf8'.format(
                   db_config['user_name'],
                   db_config['password'],
                   db_config['host'],
		   db_config['port'],
                   db_config['db_name'],
)

ENGINE = create_engine(
    DATABASE,
    encoding = "utf-8",
    echo=False # Trueだと実行のたびにSQLが出力される
)

# Sessionの作成
session = scoped_session(sessionmaker(
			autocommit = False,
			autoflush = False,
			bind = ENGINE
			)
)

# modelで使用する
Base = declarative_base()
Base.query = session.query_property()
