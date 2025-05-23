from flask import Flask, request, render_template
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)

with open('C:\\Users\\HAPPY\\Downloads\\HeartDisease\\HeartDisease\\model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)
with open('C:\\Users\\HAPPY\\Downloads\\HeartDisease\\HeartDisease\\scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    age = request.form['age']
    gender = request.form['gender']
    blood_pressure = request.form['blood_pressure']
    cholesterol_level = request.form['cholesterol_level']
    exercise_habits = request.form['exercise_habits']
    smoking = request.form['smoking']
    family_heart_disease = request.form['family_heart_disease']
    diabetes = request.form['diabetes']
    bmi = request.form['bmi']
    high_blood_pressure = request.form['high_blood_pressure']
    low_hdl_cholesterol = request.form['low_hdl_cholesterol']
    high_ldl_cholesterol = request.form['high_ldl_cholesterol']
    alcohol_consumption = request.form['alcohol_consumption']
    stress_level = request.form['stress_level']
    sleep_hours = request.form['sleep_hours']
    sugar_consumption = request.form['sugar_consumption']
    triglyceride_level = request.form['triglyceride_level']
    fasting_blood_sugar = request.form['fasting_blood_sugar']
    crp_level = request.form['crp_level']
    homocysteine_level = request.form['homocysteine_level']

    data = [
        int(age),
        int(gender),
        int(blood_pressure),
        int(cholesterol_level),
        int(exercise_habits),
        int(smoking),
        int(family_heart_disease),
        int(diabetes),
        int(bmi),
        int(high_blood_pressure),
        int(low_hdl_cholesterol),
        int(high_ldl_cholesterol),
        int(alcohol_consumption),
        int(stress_level),
        int(sleep_hours),
        int(sugar_consumption),
        int(triglyceride_level),
        int(fasting_blood_sugar),
        int(crp_level),
        int(homocysteine_level)
    ]

    # Convert to DataFrame with column names matching training
    columns = ['Age', 'Gender', 'Blood Pressure', 'Cholesterol Level', 'Exercise Habits', 
               'Smoking', 'Family Heart Disease', 'Diabetes', 'BMI', 'High Blood Pressure', 
               'Low HDL Cholesterol', 'High LDL Cholesterol', 'Alcohol Consumption', 
               'Stress Level', 'Sleep Hours', 'Sugar Consumption', 'Triglyceride Level', 
               'Fasting Blood Sugar', 'CRP Level', 'Homocysteine Level']
    new_data = pd.DataFrame([data], columns=columns)

    # Scale all features (since training scaled all columns with X = sc.fit_transform(X))
    new_data = scaler.transform(new_data)

    # Predict
    prediction = model.predict(new_data)[0]
    result = "Yes" if prediction == 1 else "No"

   
    return render_template('index.html', prediction_text=f'Prediction: Heart Disease = {result}')

if __name__ == '__main__':
    app.run(debug=True)