from infra.config import DBConnectionHandler
from infra.models import Users


class UserRepository:
    """User Reposiory"""

    @classmethod
    def insert_user(cls):
        with DBConnectionHandler() as db_conn:
            try:
                new_user = Users(name="João Marco", password="123456")
                db_conn.session.add(new_user)
                db_conn.session.commit()
            except:
                db_conn.session.rollback()
                raise
            finally:
                db_conn.session.close()

    @classmethod
    def list_user(cls):
        with DBConnectionHandler() as db_conn:
            try:
                data = db_conn.session.query(Users).filter_by(id=1).one()
                return data

            except:
                db_conn.session.rollback()
                raise
            finally:
                db_conn.session.close()
