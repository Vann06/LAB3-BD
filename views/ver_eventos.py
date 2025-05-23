import streamlit as st
import pandas as pd
from core.db import engine

def pantalla():
    st.subheader("Lista de Eventos Resumen")

    try:
        df = pd.read_sql("SELECT * FROM eventos_resumen", engine)
        st.dataframe(df)
    except Exception as e:
        st.error(f" Error al cargar la vista: {e}")
