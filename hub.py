import streamlit as st

st.set_page_config(page_title="FacialGym", layout="wide")

st.title("FacialGym — Sistema de Reconhecimento Facial")
st.markdown("Selecione uma das opções abaixo:")
st.divider()

col1, col2 = st.columns(2)

with col1:
    if st.button("Cadastrar Novo Usuário", use_container_width=True):
        st.switch_page("pages/1_FaceCaptureScreen.py")

with col2:
    if st.button("Reconhecer Usuário", use_container_width=True):
        st.switch_page("pages/2_RecognitionScreen.py")

st.divider()

st.caption("Sistema de autenticação por reconhecimento facial para academias.")
