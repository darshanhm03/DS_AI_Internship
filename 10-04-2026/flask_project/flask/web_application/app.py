from flask import Flask, request, render_template, redirect, url_for
import joblib
import numpy as np

# 1. Create Flask app instance and secret key
app = Flask(__name__)
app.config['SECRET_KEY'] = 'abalone-secret-key-123'

# 2. Define the prediction function
def predict_age(model, data):
    features = [[
        float(data['length']),
        float(data['diameter']),
        float(data['height']),
        float(data['whole_weight'])
    ]]
    prediction = model.predict(features)
    return round(float(prediction[0]), 2)

# 3. Load the pre-trained model
model = joblib.load('abalone_predictor.joblib')

# 4. Home page - shows the input form
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get form data
        data = {
            'length': request.form.get('length'),
            'diameter': request.form.get('diameter'),
            'height': request.form.get('height'),
            'whole_weight': request.form.get('whole_weight')
        }
        # Make prediction
        result = predict_age(model, data)
        return redirect(url_for('prediction', age=result))
    return render_template('home.html')

# 5. Prediction result page
@app.route('/prediction')
def prediction():
    age = request.args.get('age', 'N/A')
    return render_template('prediction.html', age=age)

# 6. Run the app
if __name__ == '__main__':
    app.run(debug=True)
