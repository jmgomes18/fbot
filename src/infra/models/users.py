from sqlalchemy import Column, String, Integer
from infra.config import Base

class Users(Base):
    """Defining users table"""

    __tablename__ = "users"

    id = Column("id", Integer, primary_key=True)
    name = Column("name", String(100), nullable=False)
    password = Column("password", String(50), nullable=False)

    def __repr__(self) -> str:
        return f"Users[name{self.name}"
