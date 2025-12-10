import cv2
import os
import numpy as np
import pickle

DATASET_PATH = "dataset"
MODEL_PATH = "lbph_classifier.yml"
NAMES_PATH = "face_names.pickle"

def ativarTrain():

    print("🔄 Iniciando treinamento do modelo LBPH...")

    face_samples = []
    labels = []
    id_to_name = {}

    current_label = 0

    for person_name in os.listdir(DATASET_PATH):
        person_folder = os.path.join(DATASET_PATH, person_name)

        if not os.path.isdir(person_folder):
            continue

        print(f"📂 Lendo imagens de: {person_name}")

        id_to_name[current_label] = person_name

        for img_file in os.listdir(person_folder):
            img_path = os.path.join(person_folder, img_file)

            img = cv2.imread(img_path)
            if img is None:
                print(f"⚠ Erro ao ler imagem: {img_path}")
                continue

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            face_samples.append(gray)
            labels.append(current_label)

        current_label += 1

    if len(face_samples) == 0:
        print("❌ Nenhuma imagem encontrada para treinamento!")
        return

    labels = np.array(labels)

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.train(face_samples, labels)

    recognizer.write(MODEL_PATH)

    with open(NAMES_PATH, "wb") as f:
        pickle.dump(id_to_name, f)

    print("✅ Treinamento concluído!")
    print(f"📦 Modelo salvo em: {MODEL_PATH}")
    print(f"👤 Dicionário salvo em: {NAMES_PATH}")
