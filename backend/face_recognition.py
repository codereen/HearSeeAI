import os
import json
import cv2
import numpy as np

CASCADE_PATH = "haar_face.xml"
DATASET_PATH = "dataset"
TRAINER_PATH = "trainer"

os.makedirs(DATASET_PATH, exist_ok=True)
os.makedirs(TRAINER_PATH, exist_ok=True)

cascade = cv2.CascadeClassifier(CASCADE_PATH)

if cascade.empty():
    raise RuntimeError("Could not load haar_face.xml")

recognizer = cv2.face.LBPHFaceRecognizer_create()

labels = {}


def register_face(name):

    person_folder = os.path.join(DATASET_PATH, name)
    os.makedirs(person_folder, exist_ok=True)

    camera = cv2.VideoCapture(0)

    count = 0

    print(f"Registering {name}...")

    while count < 20:

        success, frame = camera.read()

        if not success:
            continue

        gray = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2GRAY
        )

        faces = cascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5
        )

        for (x, y, w, h) in faces:

            face = gray[y:y+h, x:x+w]

            filename = os.path.join(
                person_folder,
                f"{count}.jpg"
            )

            cv2.imwrite(
                filename,
                face
            )

            count += 1

            print(f"Captured {count}/20")

            break

    camera.release()

    print(f"Captured training data for {name}.")

    train_model()


def train_model():

    global labels

    faces = []
    ids = []
    labels = {}

    current_id = 0

    for person in sorted(os.listdir(DATASET_PATH)):

        person_path = os.path.join(
            DATASET_PATH,
            person
        )

        if not os.path.isdir(person_path):
            continue

        labels[current_id] = person

        for image in os.listdir(person_path):

            image_path = os.path.join(
                person_path,
                image
            )

            img = cv2.imread(
                image_path,
                cv2.IMREAD_GRAYSCALE
            )

            if img is None:
                continue

            faces.append(img)
            ids.append(current_id)

        current_id += 1

    if len(faces) == 0:

        print("No training images found.")

        return

    recognizer.train(
        faces,
        np.array(ids)
    )

    trainer_file = os.path.join(
        TRAINER_PATH,
        "trainer.yml"
    )

    recognizer.save(trainer_file)

    labels_file = os.path.join(
        TRAINER_PATH,
        "labels.json"
    )

    with open(labels_file, "w") as file:

        json.dump(
            labels,
            file
        )

    print("Training complete.")
    print(f"People trained: {list(labels.values())}")


def load_model():

    global labels

    trainer_file = os.path.join(
        TRAINER_PATH,
        "trainer.yml"
    )

    labels_file = os.path.join(
        TRAINER_PATH,
        "labels.json"
    )

    if not os.path.exists(trainer_file):
        print("No trained face model found.")
        return False

    if not os.path.exists(labels_file):
        print("No face labels found.")
        return False

    recognizer.read(trainer_file)

    with open(labels_file, "r") as file:

        labels = json.load(file)

    labels = {
        int(key): value
        for key, value in labels.items()
    }

    print("Face model loaded.")
    print(f"Known people: {list(labels.values())}")

    return True


def recognize(frame):

    gray = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY
    )

    faces = cascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5
    )

    for (x, y, w, h) in faces:

        face = gray[y:y+h, x:x+w]

        name = "Unknown"

        try:

            label, confidence = recognizer.predict(face)

            if confidence < 80:

                name = labels.get(
                    label,
                    "Unknown"
                )

        except:

            name = "Unknown"

        cv2.rectangle(
            frame,
            (x, y),
            (x+w, y+h),
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            name,
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

    return frame