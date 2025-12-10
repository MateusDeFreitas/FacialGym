import cv2
import os
import re
from helper_functions import resize_video

def parse_name(name):
    name = re.sub(r"[^\w\s]", '', name)    
    name = re.sub(r"\s+", '_', name)    
    return name

def create_folders(final_path, final_full_path):
    if not os.path.exists(final_path):
        os.makedirs(final_path)

    if not os.path.exists(final_full_path):
        os.makedirs(final_full_path)


def ativarFaceCapture(person_name, max_samples=30):

    if not person_name or person_name.strip() == "":
        print("⚠ Nome inválido! O usuário deve informar um nome.")
        return

    person_name = parse_name(person_name)

    save_faces_path = f"dataset/{person_name}"
    save_full_path  = f"dataset_full/{person_name}"

    create_folders(save_faces_path, save_full_path)

    cam = cv2.VideoCapture(0)

    if not cam.isOpened():
        print("❌ ERRO: Não foi possível acessar a câmera.")
        return

    detector = cv2.CascadeClassifier('haarcascade-frontalface-default.xml')
    sample = 0

    print("📸 Iniciando captura... Aperte Q para capturar a foto.")

    while True:

        ret, frame = cam.read()
        if not ret:
            print("❌ ERRO ao capturar frame da câmera.")
            break

        frame = cv2.resize(frame, resize_video(frame.shape[1], frame.shape[0], 800))

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, 1.2, 5)

        for (x, y, w, h) in faces:
            roi = frame[y:y+h, x:x+w]
            roi = cv2.resize(roi, (140, 140))

            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)

            if True:
                sample += 1
                filename = f"{person_name}.{sample}.jpg"

                cv2.imwrite(f"{save_faces_path}/{filename}", roi)
                cv2.imwrite(f"{save_full_path}/{filename}", frame)

                print(f"✔ Foto capturada: {sample}/{max_samples}")

        cv2.imshow("Capturando rosto...", frame)

        if sample >= max_samples:
            print("✅ Captura concluída!")
            break

        cv2.waitKey(1)

    cam.release()
    cv2.destroyAllWindows()
