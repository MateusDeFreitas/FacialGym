import streamlit as st
from face_capture import ativarFaceCapture
from train import ativarTrain
import os
import cv2
import numpy as np

# ---------------------------------------------
# 🔍 Analisar preview para dar status dinâmico
# ---------------------------------------------
def analisar_frame(frame):
    try:
        file_bytes = np.asarray(bytearray(frame.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, 1)
    except:
        return "Erro ao ler a imagem ❌", "error"

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    detector = cv2.CascadeClassifier("haarcascade-frontalface-default.xml")

    faces = detector.detectMultiScale(gray, 1.2, 5)

    if len(faces) == 0:
        return "Nenhum rosto detectado ❌", "error"

    return "Rosto detectado ✔️", "success"


# ---------------------------------------------
# 🖼️ Página de captura
# ---------------------------------------------
def captura_main():

    st.title("📸 Captura de Fotos — FacialGym")
    st.markdown("Posicione-se corretamente para iniciar a coleta das imagens.")
    st.divider()

    # ----------------------------------------
    # 🔹 Informações do usuário
    # ----------------------------------------
    st.subheader("Informações do Usuário")
    col_info = st.columns(2)

    with col_info[0]:
        person_name = st.text_input("Nome do usuário (sem acentos):")

    with col_info[1]:
        max_samples = st.number_input(
            "Quantidade de fotos desejada:",
            min_value=1,
            max_value=200,
            value=30
        )

    st.divider()

    # ----------------------------------------
    # 🔹 Layout principal
    # ----------------------------------------
    col_left, col_right = st.columns([2, 1])

    # ========== COLUNA ESQUERDA ==========
    with col_left:
        st.subheader("Pré‑visualização")

        preview = st.camera_input("Pré‑visualização da Câmera")

        status_type = "none"

        if preview:
            st.image(preview, caption="Última captura", width=400)

            status_msg, status_type = analisar_frame(preview)

            if status_type == "success":
                st.success(status_msg)
            else:
                st.error(status_msg)
        else:
            st.info("Aguardando captura...")

        st.divider()

        # ---------- Botões ----------
        col_btn = st.columns(3)

        with col_btn[0]:
            if st.button("📸 Capturar Foto", use_container_width=True):

                if person_name.strip() == "":
                    st.error("Insira um nome para capturar as fotos.")
                    return

                if preview is None:
                    st.error("Nenhuma imagem capturada no preview.")
                    return

                if status_type != "success":
                    st.error("Nenhum rosto válido detectado no preview.")
                    return

                ativarFaceCapture(person_name, max_samples)
                st.success("Captura concluída! Atualizando miniaturas...")
                st.rerun()

        with col_btn[2]:
            if st.button("✅ Finalizar Captura", use_container_width=True):
                ativarTrain()
                st.success("Treinamento concluído!")

    # ========== COLUNA DIREITA ==========
    with col_right:
        st.subheader("Fotos Capturadas")

        dataset_path = f"dataset/{person_name}"
        total = 0

        if person_name.strip() != "" and os.path.exists(dataset_path):
            # filtrar apenas arquivos de imagem
            images = sorted([
                f for f in os.listdir(dataset_path)
                if f.lower().endswith((".jpg", ".jpeg", ".png"))
            ])

            # Exibir miniaturas em grade 3xN
            idx = 0
            while idx < len(images):
                cols = st.columns(3)
                for c in range(3):
                    if idx < len(images):
                        cols[c].image(f"{dataset_path}/{images[idx]}", width=120)
                        idx += 1
                        total += 1
        else:
            st.info("Nenhuma foto capturada ainda.")

        st.markdown(f"Total: **{total} / {max_samples}** fotos")


# Necessário para rodar a página no Streamlit
captura_main()
