import numpy as np
import streamlit as st
import pickle
from sklearn.preprocessing import StandardScaler

model = pickle.load(open('E:\python\webapp\model.sav','rb'))

def diabetes_predicition(input_data):
    input_data_as_nparray = np.asarray(input_data)
    input_data_reshape = input_data_as_nparray.reshape(1,-1)

    scaler = StandardScaler()
    std_data = scaler.fit_transform(input_data_reshape)

    prediction = model.predict(std_data)
    print(prediction)

    if prediction[0]==0:
        return "This person is non-diabetic"
    else:
        return "This person is diabetic"

def main():
    st.title("Diabetes Prediction App")

    #Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('BloodPressure levl')
    SkinThickness = st.text_input('SkinThickness value')
    Insulin = st.text_input('Insulin level')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunction value')
    Age = st.text_input('Person Age')

    diagnosis = ''

    if st.button('Submit'):
        diagnosis = diabetes_predicition([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])

    st.success(diagnosis)

if __name__ == '__main__':
    main()
