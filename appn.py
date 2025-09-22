import streamlit as st
import os

# ---- Configuración de la página ----
st.set_page_config(
    layout="wide",
    page_title="Sura Actuarial Desk",
)

# ---- Barra Lateral ----
# Las clases de Streamlit han cambiado, por lo que las reglas CSS ahora son diferentes.
# He optado por una solución más simple y robusta.
with st.sidebar:
    st.image("IMG/LOGO_mob.png.gif", use_container_width=True) # Corregido: usa el parámetro correcto
    st.markdown("### Sura Actuarial Desk")
    
    st.markdown("---")
    
    # He agregado una variable de estado para manejar la navegación entre páginas
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
    st.session_state.page = "inicio" # Página por defecto al cargar

if st.session_state.page == "inicio":
    col1, col2, col3 = st.columns([1, 4, 1])
    with col2:
        st.image("IMG/LOGO.jpg", width=400)
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

# ---- Estilos Personalizados (CSS) ----
st.markdown(
    """
    <style>
    /* Estilo para el fondo de la página */
    .stApp {
        background-color: #001f3f;
    }

    /* Estilo de la barra lateral */
    .st-emotion-cache-1d3d0q6 { /* Clase para el fondo de la sidebar */
        background-color: #00122e;
    }

    /* Estilo de los botones y texto en la sidebar */
    .st-emotion-cache-1c7v05d, .st-emotion-cache-18j13h4 { /* Clases para el texto y los botones */
        color: white;
    }

    /* Estilo para el contenido principal */
    .st-emotion-cache-h5h2a3 { /* Clase para el contenedor principal */
        padding-top: 2rem;
        padding-right: 2rem;
        padding-left: 2rem;
        padding-bottom: 2rem;
    }
    
    /* Estilo para los botones al pasar el ratón */
    .stButton>button {
        background-color: transparent !important;
        border: none !important;
        color: white !important;
        text-align: left;
    }
    .stButton>button:hover {
        background-color: #002e5e !important;
    }

    /* Estilo para los títulos */
    .stMarkdown h3 {
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

