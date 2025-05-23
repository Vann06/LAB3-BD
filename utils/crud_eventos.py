from sqlalchemy.orm import Session, joinedload
from sqlalchemy.exc import IntegrityError
from models.evento import Evento
from models.participante import Participante
from models.evento_participante import EventoParticipante
from models.tipo_evento import TipoEvento
from models.estado_inscripcion import EstadoInscripcion
from core.db import SessionLocal
from datetime import date
from typing import List, Optional, Dict

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_evento(db: Session, nombre: str, descripcion: Optional[str], fecha: date, id_tipo_evento: int, participantes_info: Optional[List[Dict[str, int]]] = None) -> Evento:
    db_evento = Evento(
        nombre=nombre,
        descripcion=descripcion,
        fecha=fecha,
        id_tipo_evento=id_tipo_evento
    )
    db.add(db_evento)
    db.flush()

    if participantes_info:
        for info in participantes_info:
            participante = db.query(Participante).filter(Participante.id == info['id_persona']).first()
            estado_inscripcion = db.query(EstadoInscripcion).filter(EstadoInscripcion.id == info['id_estado_inscripcion']).first()

            if not participante:
                db.rollback()
                raise ValueError(f"Participante con id {info['id_persona']} no encontrado.")
            if not estado_inscripcion:
                db.rollback()
                raise ValueError(f"Estado de inscripción con id {info['id_estado_inscripcion']} no encontrado.")

            db_evento_participante = EventoParticipante(
                id_evento=db_evento.id,
                id_persona=info['id_persona'],
                id_estado_inscripcion=info['id_estado_inscripcion']
            )
            db.add(db_evento_participante)
    
    try:
        db.commit()
        db.refresh(db_evento)
    except IntegrityError as e:
        db.rollback()
        raise e
    except Exception as e:
        db.rollback()
        raise e
    return db_evento

def get_evento(db: Session, evento_id: int) -> Optional[Evento]:
    """Obtiene un evento por su ID, incluyendo tipo de evento y participantes."""
    return db.query(Evento).options(
        joinedload(Evento.tipo_evento),
        joinedload(Evento.participantes).joinedload(EventoParticipante.participante),
        joinedload(Evento.participantes).joinedload(EventoParticipante.estado)
    ).filter(Evento.id == evento_id).first()

def get_eventos(db: Session, skip: int = 0, limit: int = 100) -> List[Evento]:
    """Obtiene una lista de eventos."""
    return db.query(Evento).options(joinedload(Evento.tipo_evento)).offset(skip).limit(limit).all()

def update_evento(
    db: Session, 
    evento_id: int, 
    nombre: Optional[str] = None, 
    descripcion: Optional[str] = None, 
    fecha: Optional[date] = None, 
    id_tipo_evento: Optional[int] = None,
    participantes_info: Optional[List[Dict[str, int]]] = None
) -> Optional[Evento]:
    db_evento = db.query(Evento).filter(Evento.id == evento_id).first()
    if not db_evento:
        return None

    if nombre is not None:
        db_evento.nombre = nombre
    if descripcion is not None:
        db_evento.descripcion = descripcion
    if fecha is not None:
        db_evento.fecha = fecha
    if id_tipo_evento is not None:
        tipo_ev = db.query(TipoEvento).filter(TipoEvento.id == id_tipo_evento).first()
        if not tipo_ev:
            raise ValueError(f"Tipo de evento con id {id_tipo_evento} no encontrado.")
        db_evento.id_tipo_evento = id_tipo_evento

    if participantes_info is not None:
        db.query(EventoParticipante).filter(EventoParticipante.id_evento == evento_id).delete()
        for info in participantes_info:
            participante = db.query(Participante).filter(Participante.id == info['id_persona']).first()
            estado_inscripcion = db.query(EstadoInscripcion).filter(EstadoInscripcion.id == info['id_estado_inscripcion']).first()

            if not participante:
                db.rollback()
                raise ValueError(f"Participante con id {info['id_persona']} no encontrado.")
            if not estado_inscripcion:
                db.rollback()
                raise ValueError(f"Estado de inscripción con id {info['id_estado_inscripcion']} no encontrado.")
            
            db_evento_participante = EventoParticipante(
                id_evento=db_evento.id,
                id_persona=info['id_persona'],
                id_estado_inscripcion=info['id_estado_inscripcion']
            )
            db.add(db_evento_participante)
            
    try:
        db.commit()
        db.refresh(db_evento)
    except IntegrityError as e:
        db.rollback()
        raise e
    except Exception as e:
        db.rollback()
        raise e
    return db_evento

def delete_evento(db: Session, evento_id: int) -> bool:
    """
    Elimina un evento por su ID.
    Gracias a ON DELETE CASCADE en la tabla eventos_participantes,
    las inscripciones asociadas se eliminarán automáticamente.
    """
    db_evento = db.query(Evento).filter(Evento.id == evento_id).first()
    if not db_evento:
        return False
    
    try:
        db.delete(db_evento)
        db.commit()
    except Exception as e:
        db.rollback()
        raise e
    return True

