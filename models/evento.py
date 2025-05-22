from sqlalchemy import Column, Integer, String, Text, ForeignKey, Date
from sqlalchemy.orm import relationship
from core.db import Base

class Evento(Base):
    __tablename__ = "eventos"
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text)
    fecha = Column(Date, nullable=False)
    id_tipo_evento = Column(Integer, ForeignKey("tipo_evento.id"))
    
    # Relaciones
    tipo_evento = relationship("TipoEvento", back_populates="eventos")
    participantes = relationship("EventoParticipante", back_populates="evento")
