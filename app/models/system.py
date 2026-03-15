
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class System(Base):
    __tablename__ = 'system'

    # 'system' is the unique identifier (Primary Key)
    system = Column(String, primary_key=True, unique=True, nullable=False)

    # 'system_name' is the descriptive name
    system_name = Column(String, nullable=False)

    def __repr__(self):
        return f"<System(system='{self.system}', name='{self.system_name}')>"