import streamlit as st

# Configure the page layout and title
st.set_page_config(
    layout="wide",  # Use a wide layout to give more space
    page_title="Sura Actuarial Desk",
)

# --- Sidebar ---
with st.sidebar:
    st.image("logo.png", use_column_width=True) # Replace "logo.png" with the path to your logo
    st.markdown("### Sura Actuarial Desk") # Use markdown for bold title
    
    # Navigation menu
    st.markdown("---")
    st.header("Menú de Navegación") # A header for the menu
    st.button("Generar Semántica")
    st.button("Procesa")
    st.button("Visualizar Datos")
    st.button("Reporte de Resultados")
    st.button("Configuración")

# --- Main Content Area ---
st.image("logo_main.png", use_column_width=True) # Replace with a larger logo for the main screen