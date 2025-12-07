import streamlit as st
from recognition import ativarRecognition

def reconhecimento_main():
    
    st.title("Reconhecimento Facial — FacialGym")
    st.markdown("Aponte a câmera para o rosto da pessoa para verificá‑la no sistema.")

    st.divider()

    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("Câmera ao vivo")

        frame = st.camera_input("Reconhecimento em tempo real")

        if frame:
            st.image(frame, caption="Último Frame Capturado")

            # Executa o reconhecimento
            status, nome, confianca = ativarRecognition(frame)

            if status == "permitido":
                st.success(f"Acesso Permitido ✔")
                st.success(f"Usuário: {nome}")
                st.success(f"Confiança: {confianca}")
            else:
                st.error("Acesso Negado ❌")

    with col2:
        st.subheader("Status do Sistema")

        st.info("""
        • Analisa o rosto capturado  
        • Compara com o banco de dados  
        • Exibe se a pessoa tem acesso
        """)

        st.markdown("---")
        st.caption("Usando modelo LBPH para reconhecimento facial.")

if __name__ == "__main__":
    reconhecimento_main()
