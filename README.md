# 🎓 Student Final Grade Prediction Using Machine Learning

## 📌 Overview

This project is a Machine Learning web application that predicts a student's **Final Grade** based on academic performance, learning behavior, and engagement factors. The application is built using **Python, Scikit-learn, and Streamlit** and allows users to predict student performance before the final examination.

---

## 🚀 Live Demo

**Live App:** *(https://farmanalam791467-student-performance-prediction-app-7ndizv.streamlit.app/)*

Example:

https://farmanalam791467-student-performance-prediction-app-7ndizv.streamlit.app/

---

## 📷 Project Preview

*(Add screenshots of your application here.)*

---

## ✨ Features

* 🎓 Predicts student final grades
* 📊 User-friendly Streamlit dashboard
* 🤖 Machine Learning-based prediction
* 📈 Displays prediction confidence
* 📝 Easy-to-use input form
* ⚡ Fast and responsive interface

---

## 📂 Dataset

**Dataset:** Student Performance and Learning Behavior Dataset (Kaggle)

### Features Used

* Study Hours
* Attendance
* Resources
* Extracurricular Activities
* Motivation
* Internet Access
* Gender
* Age
* Learning Style
* Online Courses
* Discussions
* Assignment Completion
* Educational Technology (EduTech)
* Stress Level

### Target Variable

* FinalGrade

  * 0 → Poor
  * 1 → Average
  * 2 → Good
  * 3 → Excellent

---

## 🧠 Machine Learning Algorithms

The following classification algorithms were implemented and compared:

* Logistic Regression
* Decision Tree Classifier
* Random Forest Classifier
* K-Nearest Neighbors (KNN)
* Gaussian Naive Bayes

---

## 🛠️ Technologies Used

* Python
* Streamlit
* Pandas
* NumPy
* Scikit-learn
* Joblib
* Matplotlib
* Seaborn

---

## 📁 Project Structure

```text
Student-Performance-Prediction/
│
├── app.py
├── final_grade_model.pkl
├── scaler.pkl
├── requirements.txt
├── README.md
└── dataset/
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/farmanalam791467/student-performance-prediction.git
```

Go to the project folder:

```bash
cd student-performance-prediction
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

## 📊 Model Performance

| Algorithm            | Accuracy |
| -------------------- | -------: |
| Logistic Regression  |   27.35% |
| Decision Tree        |   91.15% |
| Random Forest        |   92.15% |
| K-Nearest Neighbors  |   44.95% |
| Gaussian Naive Bayes |   27.81% |

**Best Model:** Random Forest Classifier

---

## 🎯 Future Improvements

* Hyperparameter tuning
* Feature engineering
* Explainable AI (SHAP/LIME)
* Batch prediction using CSV upload
* Student performance analytics dashboard
* Cloud deployment

---

## 👨‍💻 Author

**Farman Alam**

* GitHub: https://github.com/farmanalam791467

---

## 📜 License

This project is developed for educational and portfolio purposes.


