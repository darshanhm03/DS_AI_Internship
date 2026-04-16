# Abalone Age Predictor — Flask Deployment

## 📋 STEP-BY-STEP INSTRUCTIONS

---

## STEP 1: Install Python & Required Libraries

Open your terminal (Command Prompt on Windows) and run:

```
pip install flask scikit-learn joblib numpy pandas gunicorn
```

---

## STEP 2: Train and Save the Model

1. Open `build_model.ipynb` in Jupyter Notebook or Google Colab
2. Run all cells from top to bottom
3. This will automatically save the model file `abalone_predictor.joblib`
   into both `web_api/` and `web_application/` folders

---

## STEP 3: Test the Web API (Option A)

1. Open terminal and go into the `web_api` folder:
   ```
   cd web_api
   ```
2. Run the Flask app:
   ```
   python app.py
   ```
3. Open your browser and go to: `http://127.0.0.1:5000/`
4. Open Postman → New POST request → URL: `http://127.0.0.1:5000/predict`
5. In Body → raw → JSON, paste:
   ```json
   {
     "length": 0.41,
     "diameter": 0.33,
     "height": 0.10,
     "whole_weight": 0.36
   }
   ```
6. Click Send → You should see a predicted age!

---

## STEP 4: Test the Web Application (Option B)

1. Open terminal and go into `web_application` folder:
   ```
   cd web_application
   ```
2. Run the Flask app:
   ```
   python app.py
   ```
3. Open browser → `http://127.0.0.1:5000/`
4. Fill in the form and click "Predict Age"
5. You will see the predicted age on the result page!

---

## STEP 5: Deploy to Heroku

1. Create a free account at https://heroku.com
2. Download and install Heroku CLI: https://devcenter.heroku.com/categories/command-line
3. Open terminal in the folder you want to deploy (`web_api` or `web_application`)
4. Run these commands one by one:
   ```
   heroku login
   git init
   git add .
   git commit -m "first deployment"
   heroku create yourname-abalone-app
   git push heroku master
   ```
5. Your app is now live! Open the URL Heroku gives you.

---

## 📁 Folder Structure Explained

```
flask/
├── build_model.ipynb        ← Run this FIRST to create the model
├── web_api/
│   ├── abalone_predictor.joblib  ← Saved ML model (created by build_model.ipynb)
│   ├── app.py                    ← Flask API code
│   ├── Procfile                  ← Tells Heroku how to start the app
│   └── requirements.txt          ← List of Python packages needed
└── web_application/
    ├── abalone_predictor.joblib  ← Saved ML model (same as above)
    ├── app.py                    ← Flask Web App code
    ├── Procfile                  ← Tells Heroku how to start the app
    ├── requirements.txt          ← List of Python packages needed
    ├── templates/
    │   ├── home.html             ← Input form page
    │   └── prediction.html       ← Result page
    └── static/
        └── style.css             ← Styling for the web pages
```
