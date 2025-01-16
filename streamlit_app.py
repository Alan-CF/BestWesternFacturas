import streamlit as st
from file_processor import FileProcessor

fp = FileProcessor()

# Set the title of the Streamlit app
st.title("Ingresa las notas de crédito")

# File uploader for ZIP files
uploaded_file = st.file_uploader("Suba un archivo .zip", type="zip")

# Initialize a variable to store processed data
data = None

# Two buttons below the file uploader
col1, col2 = st.columns(2)

with col1:
    if st.button("Process File", type="secondary", use_container_width=True):
        if uploaded_file:
            data = fp.run(uploaded_file)  # Process the uploaded file
            st.success("File processed successfully!")
            st.write(data)  # Display the processed data
        else:
            st.error("Por favor sube un archivo .zip primero.")

with col2:
    if data is not None:
        st.download_button(
            label="Descargar",
            data=data,
            file_name="workbook.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            type="primary",
            use_container_width=True
        )
    else:
        if st.button(label="Descargar", type="primary", use_container_width=True):
            st.error("Por favor procesa el archivo primero.")
