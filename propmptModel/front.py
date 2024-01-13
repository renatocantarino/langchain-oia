import LangChainHelper as helper
import streamlit as st


st.set_page_config(layout="wide")
st.title("Gerador de LeroLero")

palavra = st.sidebar.text_area(label="Assunto aleatorio")

if palavra:
    response = helper.generate_company(palavra)
    st.text(response["company_name"])
