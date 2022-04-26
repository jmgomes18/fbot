from infra.config import DBConnectionHandler
from infra.models import Users

class UserRepository:
    """User Reposiory"""
    @classmethod
    def insert_user(cls):
        with DBConnectionHandler() as db_conn:
            try:
                new_user = Users(name='João Marco', password='123456')
                db_conn.session.add(new_user)
                db_conn.session.commit()
            except:
                db_conn.session.rollback()
                raise
            finally:
                db_conn.session.close()