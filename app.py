
import streamlit as st
import joblib
import numpy as np

model = joblib.load("spam_model.pkl")
THRESHOLD = 0.5

st.title("Spam Detector")
text = st.text_input("Enter text")
if st.button("Predict"):
    prediction = predict(text)
    st.write(prediction)
    if prediction == 'spam':
        st.write("This is a spam message")
    else:
        st.write("This is a ham message")
        