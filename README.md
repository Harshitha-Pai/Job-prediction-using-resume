# 📄 Resume Screening ML App  

A machine learning project that predicts whether a resume is **suitable for a Data Science role** or not.  
Built with **Python, Scikit-learn, and Streamlit**, this project demonstrates text preprocessing, ML model training, and interactive deployment.  

---

## 🚀 Features  
- Preprocesses resumes using **TF-IDF Vectorization**  
- Trains a **Logistic Regression model** to classify resumes  
- Provides an interactive **Streamlit web app** for testing resumes  
- Modular project structure with saved model and vectorizer  

---

## 🛠 Tech Stack  
- **Python 3.9+**  
- **Scikit-learn** – ML model training  
- **Streamlit** – Web app interface  
- **Pandas, NumPy** – Data processing  
- **Joblib** – Model persistence  

---

## ⚙️ Installation  

1. Clone the repository:  
   git clone https://github.com/<your-username>/resume-prediction.git
   cd resume-prediction

Create and activate a virtual environment (recommended):
python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate     # On Windows


Install dependencies:
pip install -r requirements.txt


Train (if needed):
Open and run notebook/train_model.ipynb

Run the web app:
streamlit run app/app.py

