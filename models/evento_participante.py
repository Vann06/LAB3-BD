# filepath: c:\Users\richi\OneDrive - UVG\2025_S1\Base_Datos_1\LAB3-BD\models\evento_participante.py
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from core.db import Base

class EventoParticipante(Base):
    __tablename__ = "eventos_participantes"
    
    id = Column(Integer, primary_key=True)
    id_evento = Column(Integer, ForeignKey("eventos.id", ondelete="CASCADE"))
    id_persona = Column(Integer, ForeignKey("participantes.id"), nullable=False)
    id_estado_inscripcion = Column(Integer, ForeignKey("estado_inscripcion.id"), nullable=False)
    
    # Relaciones
    evento = relationship("Evento", back_populates="participantes")
    participante = relationship("Participante", back_populates="eventos")
    estado = relationship("EstadoInscripcion", back_populates="inscripciones")