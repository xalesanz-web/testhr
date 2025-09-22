import streamlit as st
import os

# Función para cargar el archivo CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# ---- Configuración de la página ----
st.set_page_config(
    layout="wide",
    page_title="Sura Actuarial Desk",
)

# ---- Barra Lateral ----
with st.sidebar:
    st.image("LOGO.jpg", use_container_width=True)
    st.markdown("### Sura Actuarial Desk")
    st.markdown("---")
    
    if st.button("Generar Semántica"):
        st.session_state.page = "semantica"
    if st.button("Procesa"):
        st.session_state.page = "procesa"
    if st.button("Visualizar Datos"):
        st.session_state.page = "visualiza"
    if st.button("Reporte de Resultados"):
        st.session_state.page = "reporte"
    if st.button("Configuración"):
        st.session_state.page = "configuracion"

# ---- Contenido Principal ----
if 'page' not in st.session_state:
    st.session_state.page = "inicio"

if st.session_state.page == "inicio":
    col1, col2, col3 = st.columns([1, 4, 1])
    with col2:
        st.image("LOGO.jpg", width=400)
        st.markdown("<h1 style='text-align: center; color: white;'>Sura Actuarial Desk</h1>", unsafe_allow_html=True)
# ... [Código para las demás páginas] ...

# ---- Cargar el CSS ----
load_css("styles.css")

