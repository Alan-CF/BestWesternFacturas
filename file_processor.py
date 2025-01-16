import zipfile
import streamlit as st
from io import BytesIO
import pandas as pd


class FileProcessor:
    def __init__(self):
        self.start_row = 17
        self.template_path = 'Template Amazon.xlsx'
        pass
    
    def processZip(self, zip_file):
            try:
                with zipfile.ZipFile(BytesIO(zip_file.read())) as zf:
                    file_list = zf.namelist()

                    for file_name in file_list:
                        if file_name.endswith(('.xls', '.xlsx')):
                            with zf.open(file_name) as file:
                                try:


                                    df = pd.read_excel(file)
                                    self.start_row = processFile(df)




                                except Exception as e:
                                    st.error(f"Error reading {file_name}: {str(e)}")
                        else:
                            st.warning(f"Skipping non-Excel file: {file_name}")
            except zipfile.BadZipFile:
                st.error("Archivo invalido.")
            except Exception as e:
                st.error(f"Error procesando zip: {str(e)}")

    def processFile(file):
        pass