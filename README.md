# Sentiment Analysis App

##  Overview

This project is a Sentiment Analysis application built using Python and machine learning. It classifies user input text into positive, negative, or neutral sentiment in real time through an interactive web interface.

##  Features

* Real-time sentiment prediction
* Classifies text as Positive, Negative, or Neutral
* Confidence score for predictions
* Simple and interactive UI using Streamlit

##  Technologies Used

* Python
* Streamlit
* scikit-learn
* CountVectorizer
* Multinomial Naive Bayes

##  Workflow

1. User enters text input
2. Text is converted into numerical features using CountVectorizer
3. Features are passed to the trained Naive Bayes model
4. Model predicts sentiment and calculates confidence
5. Result is displayed on the UI

##  How to Run

1. Clone the repository
2. Install required libraries:

   ```
   pip install streamlit scikit-learn
   ```
3. Run the application:

   ```
   streamlit run app.py
   ```
4. Open in browser and test the app

##  Limitations

* Uses a small dataset for training
* May not handle complex sentences accurately
* Limited contextual understanding

##  Future Improvements

* Use larger real-world datasets
* Apply advanced NLP techniques (TF-IDF, embeddings)
* Implement deep learning models like LSTM or BERT
* Improve UI/UX

##  Project Type

Machine Learning / AI-based Application (Natural Language Processing)

