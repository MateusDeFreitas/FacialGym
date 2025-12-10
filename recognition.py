import cv2
import numpy as np
import pickle

MODEL_PATH = "lbph_classifier.yml"
NAMES_PATH = "face_names.pickle"

def ativarRecognition(frame):
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read(MODEL_PATH)

    with open(NAMES_PATH, "rb") as f:
        id_to_name = pickle.load(f)

    file_bytes = np.asarray(bytearray(frame.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face_detector = cv2.CascadeClassifier("haarcascade-frontalface-default.xml")
    faces = face_detector.detectMultiScale(gray, 1.1, 5)

    for (x, y, w, h) in faces:
        roi = gray[y:y+h, x:x+w]

        id_, confidence = recognizer.predict(roi)

        if confidence < 70:
            nome = id_to_name.get(id_, "Desconhecido")
            return "permitido", nome, round(confidence, 2)

    return "negado", None, None
