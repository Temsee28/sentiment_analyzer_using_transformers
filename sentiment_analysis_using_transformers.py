from transformers import pipeline
# UI using streamlit
import streamlit as st
# application about sentiment analysis using transformers
classifier= pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
st.title("Sentiment Analysis App")
#text=st.text_input("Enter desired text to determine the sentiment")
#if st.button("Sentiment"):
#model as select box
model=st.selectbox("Choose task",['sentiment-analysis','text-classification'])
text= st.text_area("Input Text")
if st.button("Click on RUN"):
    pipe=pipeline(model)
    result=pipe(text)
    st.json(result)