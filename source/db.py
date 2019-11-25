import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class PostgresDb(object):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
            try:

                connection = psycopg2.connect(user="postgres",
                                              password="modern23",
                                              host="127.0.0.1",
                                              port="5432",
                                              database="Kate")

                cursor = connection.cursor()
                engine = create_engine('postgresql+psycopg2://postgres:modern23@localhost/Kate')
                Session = sessionmaker(bind=engine)
                session = Session()

                print(connection.get_dsn_parameters(), "\n")

                cursor.execute("SELECT version();")
                record = cursor.fetchone()
                print("Your connection", record, "\n")

                PostgresDb._instance.connection = connection
                PostgresDb._instance.cursor = cursor
                PostgresDb._instance.sqlalchemy_session = session
                PostgresDb._instance.sqlalchemy_engine = engine

            except (Exception, psycopg2.Error) as error:
                print('Error: connection not established {}'.format(error))

        else:
            print('Connection already established')

        return cls._instance

    def __init__(self):
        self.connection = self._instance.connection
        self.cursor = self._instance.cursor
        self.sqlalchemy_session = self._instance.sqlalchemy_session
        self.sqlalchemy_engine = self._instance.sqlalchemy_engine

    def executes(self, query):
        try:
            cursor = self.cursor
            cursor.execute(query)
            result = cursor.fetchall()
        except Exception as error:
            print('error execting query "{}", error: {}'.format(query, error))
            return None
        else:
            return result

    def __del__(self):
        self.cursor.close()
        self.connection.close()
        self.sqlalchemy_session.close()


if __name__ == "__main__":
    db = PostgresDb()
