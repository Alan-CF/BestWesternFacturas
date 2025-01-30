import streamlit as st
import pandas as pd
import time
import io
from file_processor import FileProcessor


# Initialize file processor
fp = FileProcessor()

# Set the title of the Streamlit app
st.set_page_config(page_title="Facturación Best Western", page_icon="📂", layout="wide")
st.image("logo_top.png", width=250)
st.title("📂 Facturas Best Western")
st.write("Suba un archivo .zip para procesar las facturas.")

processing_speed = 5


# File uploader
uploaded_file = st.file_uploader("Suba un archivo .zip", type=["zip"],
                                 help="Asegúrese de que el archivo está en formato .zip")

# Initialize variables
processed_file = None
progress_bar = st.empty()
status_text = st.empty()

# Buttons layout
col1, col2 = st.columns(2)

with col1:
    if st.button("🚀 Procesar Archivo", type="primary", use_container_width=True):
        if uploaded_file:
            status_text.info("Procesando archivo...")

            for i in range(1, processing_speed + 1):
                time.sleep(0.2)  # Simulating processing delay
                progress_bar.progress(i / processing_speed)

            processed_file = fp.run(uploaded_file, uploaded_file.name)  # Process the file

            progress_bar.empty()
            status_text.empty()

            st.success("✅ Archivo procesado con éxito!")
        else:
            st.error("⚠️ Por favor sube un archivo .zip primero.")

with col2:
    if processed_file is not None:
        st.download_button(
            label="⬇️ Descargar Archivo Procesado",
            data=processed_file,
            file_name=f"Procesado_{uploaded_file.name}",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            type="primary",
            use_container_width=True
        )
    else:
        if st.button(label="⬇️ Descargar", type="primary", use_container_width=True):
            st.error("⚠️ Por favor procesa el archivo primero.")

st.markdown("---")
footer_col1, footer_col2 = st.columns([0.8, 0.2])
with footer_col1:
    st.markdown("**Hecho por Hanova Solutions**")
with footer_col2:
    st.image("logo_bottom.png", width=100)

