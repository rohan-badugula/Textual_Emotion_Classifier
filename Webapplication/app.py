import streamlit as st
import altair as alt
import pandas as pd
import numpy as np 
import joblib 
from keras.models import load_model
from keras.models import Sequential
from tensorflow.keras.preprocessing.sequence import pad_sequences
from keras.layers import Embedding, Bidirectional, LSTM, GRU, Dense

tokenizer = joblib.load('tokenizer.pkl')
# Model
model = load_model('biLSTM_w2v.h5')


def predict_emotion(docx):
    message = [docx]
    class_names = ['joy', 'fear', 'anger', 'sadness', 'neutral']
    seq = tokenizer.texts_to_sequences(message)
    padded = pad_sequences(seq, maxlen=500)

    pred = model.predict(padded)
    prediction = class_names[np.argmax(pred)]
    
    return prediction, pred ,class_names




def main():
    st.title("Text Emotion Classifier")
    with st.form(key = 'emotion_form'):
        raw_text = st.text_area("Type Here")
        submit_text = st.form_submit_button(label='Submit')
    if submit_text:
        col1,col2 = st.columns(2)
        prediction = predict_emotion(raw_text)[0]
        probability = predict_emotion(raw_text)[1]
        classes = predict_emotion(raw_text)[2]
        
        with col1:
            st.success("Original Text")
            st.write(raw_text)
            st.success("Prediction")
            st.write(prediction)
            st.write("Confidence: {:.2f}".format(np.max(probability)))
        with col2:
            st.success("Prediction probability")
            prob=pd.DataFrame(probability,columns=classes)
            prob = prob.T.reset_index()
            prob.columns = ["emotions","probability"]
            fig = alt.Chart(prob).mark_bar().encode(x='emotions',y='probability',color='emotions')
            st.altair_chart(fig,use_container_width=True)
        
    

    



if __name__ == '__main__':
    main()