from sqlalchemy import Column, String, Integer
from infra.config import Base


class Users(Base):
    """Defining users table"""

    __tablename__ = "users"

    id = Column("id", Integer, primary_key=True)
    name = Column("name", String(100), nullable=False)
    password = Column("password", String(50), nullable=False)

    def __init__(*args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    @property
    def columns(self):
        return [c.name for c in self.__table__.columns]

    @property
    def columnitems(self):
        return dict([(c, getattr(self, c)) for c in self.columns])

    def __repr__(self):
        return "{}({})".format(self.__class__.__name__, self.columnitems)

    def tojson(self):
        return self.columnitems
