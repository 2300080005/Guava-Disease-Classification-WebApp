from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Load Model
model = load_model("models/mobilenetv2_guava.keras")

# Class Labels
classes = [
    "Anthracnose",
    "fruit_fly",
    "healthy_guava"
]

# Disease Information
disease_info = {

    "Anthracnose": {
        "description":
        "Anthracnose is a fungal disease that causes dark sunken lesions on guava fruits and can significantly reduce fruit quality and yield.",

        "prevention":
        [
            "Remove and destroy infected fruits and plant debris.",
            "Prune branches to improve air circulation.",
            "Avoid overhead irrigation to reduce moisture on fruits.",
            "Apply recommended fungicides during disease-prone seasons.",
            "Use disease-free planting material."
        ]
    },

    "fruit_fly": {
        "description":
        "Fruit flies lay eggs inside guava fruits. The larvae feed on the pulp, causing rotting and making the fruit unfit for consumption.",

        "prevention":
        [
            "Collect and destroy fallen and infested fruits.",
            "Use pheromone traps to monitor and reduce fruit fly populations.",
            "Bag fruits during development to prevent egg laying.",
            "Maintain orchard sanitation.",
            "Apply approved insecticides when necessary."
        ]
    },

    "healthy_guava": {
        "description":
        "The fruit appears healthy with no visible disease symptoms.",

        "prevention":
        [
            "Maintain regular orchard hygiene.",
            "Monitor plants periodically for early disease detection.",
            "Provide balanced fertilization and irrigation.",
            "Remove diseased plant material promptly.",
            "Follow integrated pest management practices."
        ]
    }
}

@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None
    confidence = None
    filename = None
    description = None
    prevention = None

    if request.method == "POST":

        file = request.files["image"]

        if file:

            filepath = os.path.join(
                app.config["UPLOAD_FOLDER"],
                file.filename
            )

            file.save(filepath)

            # Image Preprocessing
            img = image.load_img(
                filepath,
                target_size=(224, 224)
            )

            img_array = image.img_to_array(img)

            img_array = img_array / 255.0

            img_array = np.expand_dims(
                img_array,
                axis=0
            )

            # Prediction
            preds = model.predict(img_array)

            prediction = classes[np.argmax(preds)]

            confidence = round(
                np.max(preds) * 100,
                2
            )

            description = disease_info[prediction]["description"]

            prevention = disease_info[prediction]["prevention"]

            filename = file.filename

    return render_template(
        "index.html",
        prediction=prediction,
        confidence=confidence,
        filename=filename,
        description=description,
        prevention=prevention
    )
if __name__ == "__main__":
    app.run(debug=True)