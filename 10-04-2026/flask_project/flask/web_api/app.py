from flask import Flask, request, jsonify
import joblib
import numpy as np

# 1. Create Flask app instance
app = Flask(__name__)

# 2. Define the prediction function
def predict_age(model, data):
    features = [[
        data['length'],
        data['diameter'],
        data['height'],
        data['whole_weight']
    ]]
    prediction = model.predict(features)
    return round(float(prediction[0]), 2)

# 3. Load the pre-trained model
model = joblib.load('abalone_predictor.joblib')

# 4. Home page route
@app.route('/')
def home():
    return '<h1>Abalone Age Predictor API</h1><p>Send a POST request to /predict with JSON data.</p>'

# 5. Prediction route - accepts JSON POST requests
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    prediction = predict_age(model, data)
    return jsonify({'predicted_age': prediction})

# 6. Run the app
if __name__ == '__main__':
    app.run(debug=True)
