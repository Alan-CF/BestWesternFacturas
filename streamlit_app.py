import streamlit as st
from file_processor import FileProcessor

fp = FileProcessor()

# Set the title of the Streamlit app
st.title("Ingresa las notas de credito")

# File uploader for ZIP files
uploaded_file = st.file_uploader("Suba un archivo .zip", type="zip")

# Two buttons below the file uploader
col1, col2 = st.columns(2)



with col1:
    if st.button("Process File", type="secondary", use_container_width=True):
        if uploaded_file:
            fp.processZip(uploaded_file)
        else:
            st.error("Please upload a ZIP file first.")

with col2:
    if st.button("Descargar", type="primary", use_container_width=True):
        pass

