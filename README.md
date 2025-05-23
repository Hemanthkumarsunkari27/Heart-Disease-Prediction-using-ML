# ❤️ Heart Disease Prediction System using Machine Learning

This project is a web-based application that predicts the risk of heart disease based on user input using a trained machine learning model. It utilizes Flask (or FastAPI) as a backend and Bootstrap for a responsive, animated frontend interface.

## 🚀 Features

- Predicts heart disease risk using 20 health-related attributes
- User-friendly HTML form with Bootstrap styling and animation
- Python backend (Flask/FastAPI) for real-time prediction
- Clean, informative input fields with medical context
- Ready for integration with models trained on real-world data

## 🧠 Input Attributes

1. Age (e.g., 18–100)  
2. Gender (0: Male, 1: Female)  
3. Blood Pressure (Normal: 90/60 mmHg to 120/80 mmHg)  
4. Cholesterol Level (Desirable: < 200 mg/dL)  
5. Exercise Habits (0: High, 1: Low)  
6. Smoking (0: No, 1: Yes)  
7. Family History of Heart Disease (0: No, 1: Yes)  
8. Diabetes (0: No, 1: Yes)  
9. BMI (Healthy: 18.5–24.9)  
10. High Blood Pressure (0: No, 1: Yes)  
11. Low HDL Cholesterol (0: No, 1: Yes)  
12. High LDL Cholesterol (0: No, 1: Yes)  
13. Alcohol Consumption (0: High, 1: Low, 2: Medium)  
14. Stress Level (0: High, 1: Low, 2: Medium)  
15. Sleep Hours (Recommended: 7–9 hrs)  
16. Sugar Consumption (0: High, 1: Low, 2: Medium)  
17. Triglyceride Level (mg/dL)  
18. Fasting Blood Sugar (mg/dL)  
19. CRP Level (mg/L)  
20. Homocysteine Level (µmol/L)  

## 🛠️ Technologies Used

- Python 3.x  
- Scikit-learn  
- Flask / FastAPI  
- HTML5, CSS3, Bootstrap  
- JavaScript (for UI enhancements)

## 📁 File Structure

/project-root
│

├── model.pkl # Trained ML model
├── app.py # Flask/FastAPI backend
├── templates/
│ └── index.html # Bootstrap-based form
├── static/
│ └── style.css # Custom styles and animations
└── README.md # Project overview


## ▶️ How to Run

1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the backend server: `python app.py`
4. Open your browser and go to `http://127.0.0.1:5000`

## 📊 Model Info

- Algorithm used: (e.g., Logistic Regression, Random Forest, etc.)
- Trained on: Synthetic Heart Disease Dataset with 10,000 records

## 📌 Future Scope

- Deploy on cloud (Render, Heroku, etc.)
- Integrate with a real-time health monitoring app
- Improve model accuracy using deep learning or ensemble models

## 👨‍⚕️ Disclaimer

This tool is for educational purposes only. It is **not** a substitute for professional medical advice or diagnosis.



