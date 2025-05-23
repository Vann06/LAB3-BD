import streamlit as st
from views import crear_evento, ver_eventos, editar_evento, eliminar_evento

st.set_page_config(page_title="Gestión de Eventos", layout="wide")
st.title("Sistema de Gestión de Eventos")

# Menú lateral tipo hamburguesa con botones individuales
st.sidebar.title("Menú")
st.sidebar.markdown("Selecciona una acción")

# Crear espacio en sesión para guardar la acción activa
if "vista_activa" not in st.session_state:
    st.session_state["vista_activa"] = None

if st.sidebar.button("Crear Evento"):
    st.session_state["vista_activa"] = "crear"

if st.sidebar.button("Ver Eventos"):
    st.session_state["vista_activa"] = "ver"

if st.sidebar.button("Editar Evento"):
    st.session_state["vista_activa"] = "editar"

if st.sidebar.button("Eliminar Evento"):
    st.session_state["vista_activa"] = "eliminar"

# Renderiza la vista activa
vista = st.session_state["vista_activa"]

if vista == "crear":
    crear_evento.pantalla()

elif vista == "ver":
    ver_eventos.pantalla()

elif vista == "editar":
    editar_evento.pantalla()

elif vista == "eliminar":
    eliminar_evento.pantalla()
