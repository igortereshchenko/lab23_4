from source.db import PostgresDb
from source.ormmodel import ormPlace


class UserHelper:

    def __init__(self):
        self.db = PostgresDb()

    @property
    def test(self):
        query = 'select * from public.place;'
        results = self.db.executes(query)
        print(results)
        return results


if __name__ == '__main__':
    db = PostgresDb()
    place = UserHelper()
    place.test()

    result = db.sqlalchemy_session.query(ormPlace).all()
    for row in result:
        print(row.place_site)
