import streamlit as st
import os

# ---- Cargar el CSS desde el archivo ----
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
    st.image("IMG/LOGO.jpg", use_container_width=True)
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

# ---- Contenido Principal (Basado en la selección del menú) ----
if 'page' not in st.session_state:
    st.session_state.page = "inicio"

if st.session_state.page == "inicio":
    col1, col2, col3 = st.columns([1, 4, 1])
    with col2:
        st.image("IMG/LOGO.jpg", width=400) # La imagen principal ahora se muestra
        st.markdown("<h1 style='text-align: center; color: white;'>Sura Actuarial Desk</h1>", unsafe_allow_html=True)
elif st.session_state.page == "semantica":
    st.markdown("<h1 style='color: white;'>Generar Semántica</h1>", unsafe_allow_html=True)
    st.write("Aquí puedes generar la semántica.")
elif st.session_state.page == "procesa":
    st.markdown("<h1 style='color: white;'>Procesa</h1>", unsafe_allow_html=True)
    st.write("Aquí puedes procesar datos.")
elif st.session_state.page == "visualiza":
    st.markdown("<h1 style='color: white;'>Visualizar Datos</h1>", unsafe_allow_html=True)
    st.write("Aquí puedes visualizar los datos.")
elif st.session_state.page == "reporte":
    st.markdown("<h1 style='color: white;'>Reporte de Resultados</h1>", unsafe_allow_html=True)
    st.write("Aquí puedes generar un reporte.")
elif st.session_state.page == "configuracion":
    st.markdown("<h1 style='color: white;'>Configuración</h1>", unsafe_allow_html=True)
    st.write("Aquí puedes configurar la herramienta.")

# ---- Cargar el CSS después de los componentes para que se apliquen los estilos
load_css("styles.css")
