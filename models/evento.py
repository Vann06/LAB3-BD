from sqlalchemy import Column, Integer, String, Text, ForeignKey, Date, Enum
from sqlalchemy.orm import relationship
from core.db import Base
import enum

class EstadoEvento(enum.Enum):
    planificado = "planificado"
    activo = "activo"
    cancelado = "cancelado"
    finalizado = "finalizado"

class Evento(Base):
    __tablename__ = "eventos"
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text)
    fecha = Column(Date, nullable=False)
    id_tipo_evento = Column(Integer, ForeignKey("tipo_evento.id"))
    estado = Column(Enum(EstadoEvento), default=EstadoEvento.planificado)
    
    # Relaciones
    tipo_evento = relationship("TipoEvento", back_populates="eventos")
    participantes = relationship("EventoParticipante", back_populates="evento")
