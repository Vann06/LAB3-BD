import streamlit as st
from utils.crud_eventos import get_evento, update_evento
from core.db import SessionLocal
from models.tipo_evento import TipoEvento
from models.participante import Participante
from models.estado_inscripcion import EstadoInscripcion
from models.evento import EstadoEvento

def pantalla():
    st.subheader("Editar Evento")
    db = SessionLocal()

    if "evento_id_editar" not in st.session_state:
        st.session_state["evento_id_editar"] = None
    if "evento_cargado" not in st.session_state:
        st.session_state["evento_cargado"] = None

    evento_id = st.number_input("ID del evento a editar", min_value=1, step=1)
    if st.button("Cargar evento"):
        evento = get_evento(db, evento_id)
        if evento:
            st.session_state["evento_id_editar"] = evento_id
            st.session_state["evento_cargado"] = evento
        else:
            st.error("Evento no encontrado")

    evento = st.session_state.get("evento_cargado")

    if evento:
        tipos = db.query(TipoEvento).all()
        participantes = db.query(Participante).all()
        estados = db.query(EstadoInscripcion).all()

        with st.form("form_editar_evento"):
            nombre = st.text_input("Nombre", value=evento.nombre)
            descripcion = st.text_area("Descripción", value=evento.descripcion or "")
            fecha = st.date_input("Fecha", value=evento.fecha)

            tipo_nombre = next((t.nombre for t in tipos if t.id == evento.id_tipo_evento), "")
            tipo = st.selectbox("Tipo de evento", [t.nombre for t in tipos], index=[t.nombre for t in tipos].index(tipo_nombre))
            tipo_id = next(t.id for t in tipos if t.nombre == tipo)

            estado_actual = evento.estado.value if hasattr(evento.estado, 'value') else 'planificado'
            estado_opciones = [e.value for e in EstadoEvento]
            try:
                estado_index = estado_opciones.index(estado_actual)
            except ValueError:
                estado_index = 0  # Default a 'planificado'
            
            estado_evento = st.selectbox(
                "Estado del evento", 
                estado_opciones, 
                index=estado_index,
                help="Estado actual del evento"
            )

            with st.expander("👥 Gestión de Participantes", expanded=True):
                st.markdown("**Selecciona participantes y configura su estado de inscripción:**")

                seleccionados = st.multiselect(
                    "Participantes",
                    [f"{p.nombre} {p.apellido}" for p in participantes],
                    default=[f"{ep.participante.nombre} {ep.participante.apellido}" for ep in evento.participantes]
                )

                participantes_info = []
                for seleccion in seleccionados:
                    persona = next((p for p in participantes if f"{p.nombre} {p.apellido}" == seleccion), None)
                    if persona:
                        estado_actual = next((ep.estado.nombre for ep in evento.participantes if ep.participante.id == persona.id), None)
                        estado_nombre = st.selectbox(
                            f"Estado de inscripción para {persona.nombre} {persona.apellido}",
                            [e.nombre for e in estados],
                            index=[e.nombre for e in estados].index(estado_actual) if estado_actual else 0,
                            key=f"estado_edit_{persona.id}"
                        )
                    estado_id = next((e.id for e in estados if e.nombre == estado_nombre), None)
                    participantes_info.append({
                        "id_persona": persona.id,
                        "id_estado_inscripcion": estado_id
                    })

            submit = st.form_submit_button("Actualizar evento")

            if submit:
                try:
                    update_evento(
                        db,
                        evento.id,
                        nombre=nombre,
                        descripcion=descripcion,
                        fecha=fecha,
                        id_tipo_evento=tipo_id,
                        participantes_info=participantes_info
                    )
                    st.success("Evento actualizado")
                    st.session_state["evento_cargado"] = None
                except Exception as e:
                    st.error(f"Error al actualizar: {e}")
