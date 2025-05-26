import streamlit as st
from core.db import SessionLocal
from models.tipo_evento import TipoEvento
from models.participante import Participante
from models.estado_inscripcion import EstadoInscripcion
from utils.crud_eventos import create_evento
from models.evento import EstadoEvento

def pantalla():
    st.subheader("Crear Evento")
    db = SessionLocal()

    tipos = db.query(TipoEvento).all()
    participantes = db.query(Participante).all()
    estados = db.query(EstadoInscripcion).all()

    # Usar Pendiente como estado para todos los participantes
    estado_id_pendiente = next((e.id for e in estados if e.nombre.lower() == "pendiente"), None)

    if estado_id_pendiente is None:
        st.error("No se encontró el estado 'Pendiente' en la base de datos.")
        return

    with st.form("form_crear_evento"):
        nombre = st.text_input("Nombre del evento")
        descripcion = st.text_area("Descripción")
        fecha = st.date_input("Fecha del evento")
        estado_opciones = [e.value for e in EstadoEvento]
        estado = st.selectbox("Estado del evento", estado_opciones)

        tipo_nombres = [t.nombre for t in tipos]
        tipo_nombre = st.selectbox("Tipo de evento", tipo_nombres)
        tipo_id = next((t.id for t in tipos if t.nombre == tipo_nombre), None)

        participantes_nombres = [f"{p.nombre} {p.apellido}" for p in participantes]
        seleccionados = st.multiselect("Participantes", participantes_nombres)
        participantes_ids = [p.id for p in participantes if f"{p.nombre} {p.apellido}" in seleccionados]

        submit = st.form_submit_button("Crear evento")

        if submit:
            if not nombre or not participantes_ids:
                st.error("Completa todos los campos obligatorios.")
            else:
                participantes_info = [
                    {
                        "id_persona": pid,
                        "id_estado_inscripcion": estado_id_pendiente
                    }
                    for pid in participantes_ids
                ]
                try:
                    create_evento(db, nombre, descripcion, fecha, tipo_id, participantes_info)
                    st.success("Evento creado con éxito")
                except Exception as e:
                    st.error(f"Error al crear: {e}")
