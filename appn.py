import streamlit as st
import os

# --- 1. Clonar el repositorio para acceder a la imagen ---
# Esto solo se ejecutará una vez al inicio.
# Se asume que el repositorio se clonará en la misma carpeta donde se ejecuta app.py
if not os.path.exists("IMG/LOGO.jpg"):
    # Si aún no hemos clonado el repositorio, lo hacemos.
    # En un entorno de Colab real, esto iría en una celda separada antes de ejecutar el script.
    # Aquí lo pongo por si acaso, pero lo ideal es clonar el repo en una celda anterior.
    st.warning("Clonando repositorio para acceder a las imágenes. Por favor, asegúrate de haberlo hecho en una celda anterior para evitar este mensaje.")
    # Si tu app.py está en el root del repo, entonces el path a IMG/LOGO.jpg es directo.
    # Si app.py está en una subcarpeta, deberás ajustar los paths.
    
    # Este comando solo funcionaría si app.py está en la raíz de un repo clonado.
    # Para la ejecución en Colab, es mejor que el git clone sea una celda previa.
    # Por simplicidad, asumo que IMG/LOGO.jpg estará disponible.
    pass # Eliminamos el git clone de aquí, ya que se hará en Colab previamente.


# ---- 2. Configuración de la página ----
# Usa un diseño amplio y establece el título de la página
st.set_page_config(
    layout="wide",
    page_title="Sura Actuarial Desk",
)

# ---- 3. Barra Lateral ----
# Todo lo que esté en este bloque se mostrará en la barra lateral
with st.sidebar:
    st.image("IMG/LOGO.jpg", use_column_width=True) # Usa tu logo aquí
    st.markdown("### Sura Actuarial Desk")
    
    # Separador visual
    st.markdown("---")
    
    # Botones de navegación
    st.button("Generar Semántica")
    st.button("Procesa")
    st.button("Visualizar Datos")
    st.button("Reporte de Resultados")
    st.button("Configuración")

# ---- 4. Contenido Principal ----
# Usa columnas para centrar el contenido principal
# La primera y última columna son para espacio en blanco
col1, col2, col3 = st.columns([1, 4, 1])

with col2:
    # Muestra el logo más grande y el título en el centro
    st.image("IMG/LOGO.jpg", width=400) # Ajusta el ancho según necesites
    st.markdown("<h1 style='text-align: center;'>Sura Actuarial Desk</h1>", unsafe_allow_html=True)
    
# ---- 5. Estilos Personalizados (CSS) ----
# Aquí ajustamos los colores para que coincidan con tu imagen
st.markdown(
    """
    <style>
    /* Estilos generales para el fondo de la página */
    .stApp {
        background-color: #001f3f; /* Azul oscuro similar al de tu imagen */
    }

    /* Estilo de la barra lateral */
    .css-1d3f8gv.e1fqkh3o1 { /* Clase específica para el fondo de la sidebar */
        background-color: #00122e; /* Azul aún más oscuro para la sidebar */
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    /* Estilo para el texto blanco en la sidebar */
    .sidebar .st-bb { /* Botones */
        color: white !important;
    }
    .sidebar .stButton>button {
        color: white !important;
        border: none !important;
        background-color: transparent !important;
        text-align: left;
        width: 100%;
        padding-left: 1rem;
    }
    .sidebar .stButton>button:hover {
        background-color: #002e5e !important; /* Un poco más claro al pasar el ratón */
    }
    
    /* Estilo para los títulos en la sidebar */
    .sidebar h3, .sidebar h2, .sidebar h1 {
        color: white !important;
        text-align: left;
        padding-left: 1rem;
    }
    .sidebar .stMarkdown p { /* Texto markdown en la sidebar */
        color: white !important;
        padding-left: 1rem;
    }

    /* Estilo para el contenido principal */
    .main .block-container {
        padding-top: 2rem;
        padding-right: 2rem;
        padding-left: 2rem;
        padding-bottom: 2rem;
    }
    .main h1 { /* Título principal */
        color: white !important;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)
