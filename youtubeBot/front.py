import ytHelper as helper
import streamlit as st
import textwrap


st.set_page_config(layout="wide")
st.title("Assistente do YT")

with st.sidebar:
    with st.form(key="my_form"):
        submit = st.form_submit_button(label="enviar")
        url = st.sidebar.text_area(label="Url do video" , max_chars=200)
        query = st.sidebar.text_area(key="query" ,  label="Me pergunte algo do video" , max_chars=200)
     
if query and url:
    db = helper.create_vector_from_yt_url(url)        
    response, docs = helper.get_response_from_query(db, query)
    st.subheader("resposta")
    st.text(textwrap.fill(response["answer"]))


