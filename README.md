# 🍈 Guava Disease Classification System

## Overview

The Guava Disease Classification System is a deep learning-based web application that detects diseases in guava fruits using image classification. The application allows users to upload a guava fruit image and predicts whether it belongs to one of the following categories:

* Anthracnose
* Fruit Fly
* Healthy Guava

The project uses a MobileNetV2 transfer learning model trained on a guava disease dataset and deployed through a Flask web application.

---

## Features

* Upload guava fruit images through a web interface
* Real-time disease prediction
* Confidence score display
* Disease description
* Preventive measures and recommendations
* User-friendly Flask web application

---

## Dataset Information

Dataset: Guava Disease Dataset

Classes:

1. Anthracnose
2. Fruit Fly
3. Healthy Guava

Dataset Statistics:

| Class         | Train | Validation | Test |
| ------------- | ----: | ---------: | ---: |
| Anthracnose   |  1080 |        308 |  156 |
| Fruit Fly     |   918 |        262 |  132 |
| Healthy Guava |   649 |        185 |   94 |

Total Images: 3784

Image Size: 224 × 224 pixels

---

## Technologies Used

* Python
* TensorFlow
* Keras
* Flask
* NumPy
* Pillow
* Bootstrap 5

---

## Model Performance

| Model       | Accuracy |
| ----------- | -------: |
| Simple CNN  |   94.24% |
| MobileNetV2 |   98.95% |

MobileNetV2 was selected as the final model due to its superior performance and lower misclassification rate.

---

## Project Structure

```text
GuavaDiseaseWebApp/
│
├── app.py
├── requirements.txt
├── README.md
│
├── models/
│   └── mobilenetv2_guava.keras
│
├── static/
│   └── uploads/
│
└── templates/
    └── index.html
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd GuavaDiseaseWebApp
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the Flask application:

```bash
python app.py
```

Open the application in your browser:

```text
http://127.0.0.1:5000
```

---

## How It Works

1. User uploads a guava fruit image.
2. Image is resized to 224 × 224 pixels.
3. Pixel values are normalized.
4. MobileNetV2 model performs inference.
5. Predicted disease class is displayed.
6. Confidence score is shown.
7. Disease information and preventive measures are provided.

---

## Results

The MobileNetV2 model achieved:

* Test Accuracy: 98.95%
* Correct Predictions: 378 / 382
* Misclassifications: 4

The model demonstrates excellent performance in distinguishing between Anthracnose, Fruit Fly, and Healthy Guava classes.

---

## Future Enhancements

* AWS EC2 Deployment
* AWS S3 Integration
* SageMaker Endpoint Deployment
* Multi-language Support
* Mobile Application Integration
* Disease Severity Detection

---

## Author

Sudheer Boddeti

B.Tech – Artificial Intelligence & Data Science

AWS Certified Cloud Practitioner

AWS Certified Machine Learning Engineer – Associate
