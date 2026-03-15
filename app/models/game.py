
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class SystemConfig(Base):
    __tablename__ = 'game'

    game_id = Column(Integer, primary_key=True, autoincrement=True)
    system = Column(String, nullable=False) # Foreign key to system
    game_name = Column(String, nullable=False) # derived from the ROM file name
    rom_path = Column(String, nullable=False) # full path to the ROM file including the file name
    added_date = Column(DateTime, nullable=False)

    def __repr__(self):
        return f"<Game(game_id='{self.game_id}', name='{self.game_name}')>"