from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# postgresql://{user}:{password}@{host}:{port}/{database}?sslmode=require
class DBConnectionHandler:
    """Sqlalchemy database connection"""

    def __init__(self):
        self.__connection_string = "mysql+pymysql://admin:3yK1gwZCYBx42NBpt449@fbot-api.c4xmwex5k2jk.sa-east-1.rds.amazonaws.com/fbot_api"
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
