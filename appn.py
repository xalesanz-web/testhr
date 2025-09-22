import streamlit as st

# ---- Configuración de la página ----
# Usa un diseño amplio y establece el título de la página
st.set_page_config(
    layout="wide",
    page_title="Sura Actuarial Desk",
)

# ---- Barra Lateral ----
# Todo lo que esté en este bloque se mostrará en la barra lateral
with st.sidebar:
    # Puedes poner el logo aquí si lo tienes guardado como un archivo
    # st.image("logo_sura_sidebar.png", use_column_width=True)
    st.markdown("## GRUPO SURA")
    st.markdown("---")
    st.markdown("### Sura Actuarial Desk")
    st.markdown("---")
    
    # Botones de navegación
    st.button("Generar Semántica")
    st.button("Procesa")
    st.button("Visualizar Datos")
    st.button("Reporte de Resultados")
    st.button("Configuración")

# ---- Contenido Principal ----
# Aquí va el contenido de la pantalla principal
col1, col2, col3 = st.columns([1, 4, 1])

with col2:
    # Puedes colocar el logo grande aquí
    # st.image("logo_sura_main.png", width=400)
    st.markdown("<h1 style='text-align: center;'>Sura Actuarial Desk</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center;'>GRUPO SURA</h1>", unsafe_allow_html=True)

# ---- Notas Adicionales ----
st.markdown("""
<style>
.reportview-container .main .block-container {
    padding-top: 2rem;
    padding-right: 2rem;
    padding-left: 2rem;
    padding-bottom: 2rem;
}
.sidebar .sidebar-content {
    background-color: #00122e; /* Color de fondo de la barra lateral */
    padding-top: 2rem;
    padding-bottom: 2rem;
}
</style>
""", unsafe_allow_html=True)
