from sqlalchemy import Column, Integer, String, Text, ForeignKey, Date
from sqlalchemy.orm import relationship
from core.db import Base

class Participante(Base):
    __tablename__ = "participantes"
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    correo = Column(String(100), unique=True)
    
    # Relación con eventos_participantes
    eventos = relationship("EventoParticipante", back_populates="participante")

