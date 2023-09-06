import streamlit as st
import translator4 as translator
from PyPDF2 import PdfReader


User_API = st.text_input (label = "API KEY")
uploaded_file = st.file_uploader(label= "To Translate", accept_multiple_files=False, type='pdf')
export_as_pdf = st.button("Translate") 



if User_API != "":
    translator.set_API(User_API)



if uploaded_file is not None:
    pdf_reader = PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    print(text)
    translation = translator.compiler(text)
    stage_two = True
    

#---------------------------------------Export Buttom---------------------------------#    

if export_as_pdf:
    html = translator.create_PDF(translation)
    st.markdown(html, unsafe_allow_html=True)