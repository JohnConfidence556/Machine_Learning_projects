# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle
import streamlit as st

# loading the saved model
loaded_model = pickle.load(open( "C:/Users/BRIGHT COMPUTERS/Desktop/machine learning projects/model_deployment/trained_model.sav", 'rb'))

# creating a function for prediction

def diabetes_prediction(input_data):
    
    # changing the input data to mumpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        return 'The person is not diabetic'
    else:
        return 'The person is diabetic'

def main():
    
    # giving a title
    st.title('Diabetes Prediction Web App')
    
    # getting the input from the user 
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Enter Glucose level')
    BloodPressure = st.text_input('Enter Blood Pressure level')
    SkinThickness = st.text_input('Enter skin thickness level')
    Insulin = st.text_input('Enter Insulin level')
    BMI = st.text_input('Enter BMI level')
    DiabetesPedigreeFunction = st.text_input('Enter Diabetes Pedigree Function value')
    Age = st.text_input('Enter Age of the patient')
    
    # code for prediction
    diagnosis = ''
    
    # creating a button for prediction
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
        
    st.success(diagnosis)
    
if __name__ == '__main__':
    main()
    
    
    
