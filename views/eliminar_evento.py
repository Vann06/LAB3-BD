import streamlit as st
from utils.crud_eventos import get_evento, delete_evento
from core.db import SessionLocal

def pantalla():
    st.subheader("Eliminar Evento")
    db = SessionLocal()

    if "evento_id_eliminar" not in st.session_state:
        st.session_state["evento_id_eliminar"] = None
    if "evento_a_eliminar" not in st.session_state:
        st.session_state["evento_a_eliminar"] = None

    evento_id = st.number_input("ID del evento a eliminar", min_value=1, step=1)
    if st.button("Cargar evento"):
        evento = get_evento(db, evento_id)
        if evento:
            st.session_state["evento_id_eliminar"] = evento_id
            st.session_state["evento_a_eliminar"] = evento
        else:
            st.error("Evento no encontrado")

    evento = st.session_state.get("evento_a_eliminar")

    if evento:
        st.warning(f"¿Deseas eliminar el evento: {evento.nombre}?")
        if st.button("Eliminar definitivamente"):
            try:
                eliminado = delete_evento(db, evento.id)
                if eliminado:
                    st.success("Evento eliminado correctamente")
                    st.session_state["evento_a_eliminar"] = None
                else:
                    st.error("No se pudo eliminar el evento")
            except Exception as e:
                st.error(f"Error al eliminar: {e}")
