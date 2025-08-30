import streamlit as st
import joblib

# Load model & vectorizer
model = joblib.load("models/resume_model.pkl")
tfidf = joblib.load("models/tfidf_vectorizer.pkl")

st.title("📄 Resume Screening App")
st.write("Upload or paste a resume to predict the job category!")

# Text input
resume_text = st.text_area("Paste resume text here:")

if st.button("Predict"):
    if resume_text.strip() != "":
        # Transform input
        input_vec = tfidf.transform([resume_text])
        prediction = model.predict(input_vec)[0]

        st.success(f"✅ Predicted Job Category: **{prediction}**")
    else:
        st.warning("⚠️ Please enter some resume text.")
