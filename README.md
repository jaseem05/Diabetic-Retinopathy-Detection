
# 🧠 Diabetic Retinopathy Detection using CNN and Flask

This project detects the severity of **Diabetic Retinopathy** from retinal fundus images using a **Convolutional Neural Network (CNN)** model. The model is deployed with a **Flask web application**, allowing users to upload images and receive predictions in real time.

## 📂 Project Structure

```
├── app.py                     # Flask application
├── dr.h5                      # Trained CNN model (ResNet34)
├── templates/
│   └── index.html             # HTML template for UI
├── static/
│   └── uploads/               # Folder to store uploaded images
├── project-1.ipynb            # Model training and preprocessing code
└── README.md
```

## 🔍 About the Dataset

We used the **APTOS 2019 Blindness Detection** dataset, which contains retinal images categorized into five classes:
- 0: No_DR
- 1: Mild
- 2: Moderate
- 3: Severe
- 4: Proliferate_DR

All images were preprocessed using **Gaussian filtering** and resized to **224x224** pixels.

## 🏗️ Model

- **Architecture**: Pretrained **ResNet34**
- **Training**: Fine-tuned for 20 epochs using FastAI
- **Output**: Probability for each of the 5 DR stages

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/diabetic-retinopathy-flask.git
cd diabetic-retinopathy-flask
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

Example `requirements.txt`:
```
flask
tensorflow
numpy
Pillow
```

### 3. Add your trained model
Place your `dr.h5` model file in the root directory.

### 4. Run the Flask App
```bash
python app.py
```

Visit `http://127.0.0.1:5000` in your browser.

## 🌐 How It Works

1. Upload a retinal image via the web interface.
2. The image is preprocessed and passed through the CNN model.
3. The model predicts one of the five DR classes.
4. The prediction is displayed along with the uploaded image.

## 📸 Screenshot

*(Add a screenshot of your web app UI here)*

## 📌 Future Work

- Improve accuracy using ensemble models
- Add model explainability using Grad-CAM
- Deploy on cloud (Heroku, AWS, etc.)

## 📃 License

This project is licensed under the MIT License.
