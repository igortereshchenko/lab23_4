from source.db import PostgresDb
from source.ormmodel import  Base

db = PostgresDb()

Base.metadata.create_all(db.sqlalchemy_engine)

session = db.sqlalchemy_session
session.commit()

session.commit()