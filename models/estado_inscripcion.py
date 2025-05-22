# filepath: c:\Users\richi\OneDrive - UVG\2025_S1\Base_Datos_1\LAB3-BD\models\estado_inscripcion.py
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from core.db import Base

class EstadoInscripcion(Base):
    __tablename__ = "estado_inscripcion"
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    
    # Relación con eventos_participantes
    inscripciones = relationship("EventoParticipante", back_populates="estado")