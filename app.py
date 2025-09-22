# Ejemplo de código con gradio

import gradio as gr

def procesar_datos(texto_entrada):
    # Aquí iría la lógica principal de tu herramienta
    # que estaba en tu código original
    resultado = f"Procesando: '{texto_entrada}'... ¡Listo!"
    return resultado

# Crea la interfaz de Gradio
interfaz = gr.Interface(
    fn=procesar_datos,
    inputs="text",
    outputs="text",
    title="Mi Herramienta en Colab",
    description="Una herramienta interactiva creada con Gradio."
)

# Lanza la interfaz
interfaz.launch()