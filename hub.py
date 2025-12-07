import streamlit as st

# Configuração da página principal
st.set_page_config(page_title="FacialGym", layout="wide")

# Título e descrição
st.title("📌 FacialGym — Sistema de Reconhecimento Facial")
st.markdown("Selecione uma das opções abaixo:")
st.divider()

# Layout dos botões principais
col1, col2 = st.columns(2)

# Botão para acessar a página de captura de fotos
with col1:
    if st.button("📸 Cadastrar Novo Usuário", use_container_width=True):
        st.switch_page("pages/1_FaceCaptureScreen.py")

# Botão para acessar a página de reconhecimento facial
with col2:
    if st.button("🧠 Reconhecer Usuário", use_container_width=True):
        st.switch_page("pages/2_RecognitionScreen.py")

st.divider()

# Rodapé
st.caption("Sistema de autenticação por reconhecimento facial para academias.")
