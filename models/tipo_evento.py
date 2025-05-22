# filepath: c:\Users\richi\OneDrive - UVG\2025_S1\Base_Datos_1\LAB3-BD\models\tipo_evento.py
from sqlalchemy import Column, Integer, String, Text, ForeignKey, Date
from sqlalchemy.orm import relationship
from core.db import Base

class TipoEvento(Base):
    __tablename__ = "tipo_evento"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text)
    eventos = relationship("Evento", back_populates="tipo_evento")
