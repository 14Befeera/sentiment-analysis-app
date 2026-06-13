import streamlit as st
from model import predict_sentiment

st.title("Sentiment Analysis App")

# User input
user_input = st.text_area("Enter your text")

# Button
if st.button("Analyze Sentiment"):
    if user_input:
        result = predict_sentiment(user_input)
        st.subheader(f"Sentiment: {result}")
    else:
        st.warning("Please enter some text!")