from datetime import datetime, timezone

from sqlalchemy import Column, String, Integer, DateTime
from app.core.database import Base

class Game(Base):
    __tablename__ = 'game'

    game_id = Column(Integer, primary_key=True, autoincrement=True)
    system = Column(String, nullable=False) # Foreign key to system
    game_name = Column(String, nullable=False) # derived from the ROM file name
    game_path = Column(String, nullable=False) # full path to the ROM file including the file name
    date_added = Column(DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))

    def __repr__(self):
        return f"<Game(game_id='{self.game_id}', name='{self.game_name}', system='{self.system}')>"