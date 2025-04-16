from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

# Create flask app
app = Flask(__name__)
model = load_model("C:\\Users\\Administrator\\Desktop\\DRD\\dr.h5")

labels = ['No_DR', 'Mild', 'Moderate', 'Severe', 'Proliferate_DR']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "No file uploaded"
    
    file = request.files['file']
    if file.filename == '':
        return "No selected file"

    filepath = os.path.join('static/uploads', file.filename)
    file.save(filepath)

    img = image.load_img(filepath, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0

    prediction = model.predict(img_array)
    predicted_class = labels[np.argmax(prediction)]

    return render_template('index.html', prediction=predicted_class, image_path=filepath)

if __name__ == "__main__":
    app.run(debug=True)