# Textual Emotion Classifier


---

## Introduction

Emotion recognition is an important task in natural language processing that involves identifying the underlying emotional state of a given text. In this project, we have developed a Text Emotion Recognition system that uses deep learning techniques to classify text into one of five emotion categories: joy, fear, anger, neutral, and sadness.

Our model is built using LSTM, a type of recurrent neural network that is particularly well-suited for processing sequential data like text. It is trained on a large dataset of annotated text data to accurately predict the emotional state of new inputs.

The project is implemented using MongoDB as the backend database and Streamlit as the frontend web application framework. MongoDB provides a scalable and flexible storage solution for the text data, while Streamlit allows users to interact with the model through an intuitive and user-friendly web interface.

---

## Data Preparation

We retrieve data from the Big_Data database, which contains two collections:
- Data_train
- Data_Test

![Picture2](https://github.com/rohan-badugula/Textual_Emotion_Classifier/assets/75232973/39e0fd6e-f5f9-483b-9570-7ac527debfcf)

Both collections contain emotion-labeled text data, with two fields for each entry: "emotion" and "sentence". We import this data as Pandas DataFrames in Python and use it to train and test our Text Emotion Recognition model, built using LSTM.

---
![WhatsApp Image 2023-07-17 at 23 06 21](https://github.com/rohan-badugula/Textual_Emotion_Classifier/assets/75232973/4f6e4550-499c-446e-b5ff-7397e2fc5024)

## Proposed Architecture

The Text Emotion Recognition model uses an embedding layer, a bidirectional LSTM layer, and a dense output layer to predict emotions in textual data. It is trained with a batch size of 128 and for 15 epochs. The model is trained on 7,934 samples and validated on 3,393 samples. The training process involves minimizing the loss function and evaluating the model's performance at each epoch using validation data. The resulting trained model accurately predicts emotions in textual data.
![Picture3](https://github.com/rohan-badugula/Textual_Emotion_Classifier/assets/75232973/36c59704-f354-4c5b-8ec2-fc246ef8d23c)

---
## Accuracy and Loss Plots

![Picture4](https://github.com/rohan-badugula/Textual_Emotion_Classifier/assets/75232973/c441bc45-8c57-418e-8162-ee36e5a2fb57)

**Accuracy:** 73.56% on the validation set.

---

## Result and Output

Our Text Emotion Recognition model takes a sentence as input and predicts the corresponding emotion label. The input sentence can be any text-based data, such as a tweet or a product review. The model then outputs a single emotion label chosen from the five possible categories:

- Joy
- Fear
- Anger
- Neutral
- Sadness

![Picture5](https://github.com/rohan-badugula/Textual_Emotion_Classifier/assets/75232973/fbfb8295-6623-4f35-8fe1-6b843e649921)

---
## Sample Prediction

![Picture6](https://github.com/rohan-badugula/Textual_Emotion_Classifier/assets/75232973/1d0a1ce1-d7ee-4521-b1d6-a1348a31f172)

---
## GUI
To make our Text Emotion Recognition system more accessible and user-friendly, we have implemented a graphical user interface (GUI) using Streamlit. This allows users to easily interact with the model through a web-based interface, without requiring any programming knowledge.

The Streamlit app takes in a sentence as input and then passes it to the Text Emotion Recognition model for prediction. The output emotion label is then displayed on the screen along with a corresponding color code for easy visualization.


![Picture7](https://github.com/rohan-badugula/Textual_Emotion_Classifier/assets/75232973/3003b32f-d007-43c9-97eb-a56566e3c672)

---

## CONCLUSION
In conclusion, our Text Emotion Recognition project is a powerful and reliable tool for identifying emotions in textual data. By utilizing deep learning techniques, specifically LSTM, we have developed a model that accurately classifies input text into one of five emotion categories. 
The project is backed by a MongoDB database and is presented using Streamlit, a web application framework for Python. This provides a scalable and flexible storage solution for the text data, while the GUI implementation makes it easy for users to interact with the model and analyze the emotional content of text data. Overall, our Text Emotion Recognition system has potential applications in various fields, including sentiment analysis, customer feedback analysis, and more.


---


Please feel free to explore the code and project repository for more details.
