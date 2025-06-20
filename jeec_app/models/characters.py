from sqlalchemy import Column, String, Integer, DateTime, func, Date, Boolean, func
from database import Base
from jeec_app.models.model_mixin import ModelMixin

class Characters(Base, ModelMixin):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    name = Column(String(100), nullable=False)
    age = Column(Integer)
    birthday = Column(Date)             # Data sem hora
    gender = Column(String(30))
    is_alive = Column(Boolean, default = True)         # 1 sim || 0 não

    #species = Column(String(100))
    #series = Column(String(100))


    def __repr__(self):
        return f"<Character {self.id}: {self.name}>"
