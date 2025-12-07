# 📌 FacialGym — Sistema de Reconhecimento Facial

FacialGym é um sistema completo de autenticação baseado em **reconhecimento facial**, desenvolvido em Python com Streamlit e OpenCV.  
Foi projetado para academias, catracas e ambientes que precisam verificar rapidamente se um usuário está cadastrado.

---

## 🚀 Funcionalidades Principais

### 🔹 1. Cadastro de Usuários
- Captura de múltiplas fotos do rosto usando webcam
- Armazenamento em duas pastas organizadas:
  - `/dataset` → faces recortadas
  - `/dataset_full` → imagens completas
- Treinamento automático do modelo LBPH após a coleta

### 🔹 2. Reconhecimento Facial
- Leitura da webcam em tempo real
- Detecção de rostos usando HaarCascade
- Identificação utilizando modelo LBPH treinado
- Exibição de mensagem:
  - **Acesso Permitido**
  - **Acesso Negado**

### 🔹 3. Interface em Streamlit
- Hub com navegação entre telas
- Tela de captura organizada e intuitiva
- Tela de reconhecimento simples e funcional

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **Streamlit**
- **OpenCV**
- **LBPH Face Recognizer**
- **NumPy**
- **Pickle** para armazenamento de IDs

---

## 📁 Estrutura do Projeto

FacialGym/ <br>
│── hub.py — Página inicial (menu principal) <br>
│ <br>
│── pages/ <br>
│    │── 1_FaceCaptureScreen.py — Tela de cadastro de novo usuário <br>
│    │── 2_RecognitionScreen.py — Tela de reconhecimento facial <br>
│ <br>
│── face_capture.py — Captura e armazenamento das fotos <br>
│── train.py — Treinamento do modelo LBPH <br>
│── recognition.py — Execução do reconhecimento facial <br>
│ <br>
│── dataset/ — Faces recortadas <br>
│    │── Nome_Usuario/ <br>
│ <br>
│── dataset_full/ — Fotos completas <br>
│    │── Nome_Usuario/ <br>
│ <br>
│── haarcascade-frontalface-default.xml <br>
│── lbph_classifier.yml — Modelo treinado <br>
│── face_names.pickle — Mapeamento ID → Nome <br>
│── helper_functions.py <br>


---

## ▶️ Como Executar

### 1. Instalar dependências
pip install streamlit opencv-python opencv-contrib-python numpy


### 2. Rodar o sistema
streamlit run hub.py


### 3. Na interface que abrir:
- Clique em **Cadastrar Novo Usuário** para capturar fotos  
- Clique em **Reconhecer Usuário** para validar o rosto  

---

## 💡 Requisitos para bom funcionamento

- Ambiente bem iluminado  
- Rosto centralizado na câmera  
- Evitar acessórios que mudem muito a aparência (óculos escuros, boné etc.)  
- Capture pelo menos **20–30 fotos** para garantir boa precisão  

---

## 📌 Objetivo do Projeto

Este é um sistema desenvolvido para estudos e demonstrações, podendo ser facilmente integrado a catracas, aplicativos de controle de acesso, sistemas de presença e muito mais.

---

## 👨‍💻 Desenvolvedores

Projeto criado por:  
- **Daniel Martins**
- **Gabriel Xavier**
- **Mateus Freitas**  
