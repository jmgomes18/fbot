import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConnectionHandler:
    """Sqlalchemy database connection"""

    def __init__(self):
        self.__database = os.environ.get("DATABASE")
        self.__host = os.environ.get("DB_HOST")
        self.__user = os.environ.get("DB_USER")
        self.__password = os.environ.get("DB_PASS")
        self.__connection_string = "mysql+pymysql://{}:{}@{}/{}".format(
            self.__user, self.__password, self.__host, self.__database
        )
        self.session = None

    def get_engine(self):
        """Return connection engine
        param: None
        return: engine connection to Database
        """
        engine = create_engine(self.__connection_string)
        return engine

    def __enter__(self):
        engine = create_engine((self.__connection_string))
        session_maker = sessionmaker()
        self.session = session_maker(bind=engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
