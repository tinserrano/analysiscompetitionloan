
import streamlit as st
import pandas as pd
import joblib
import numpy as np
from Data import *

st.title("Loan Prediction")

st.image('coins.jpeg')

st.header("Predicción sobre el comportamiento en el pago de un préstamo")
st.write("Aqui llevamos a desarrollo la competencia Loan Prediction publicada en Analytics Vidhya (https://datahack.analyticsvidhya.com/contest/practice-problem-loan-prediction-iii/) donde a partir de determinados datos de las personas, se evalua cómo sería el comportamiento en el pago de su préstamo")
st.write("A través de un modelo de machine learning podemos evaluar miles de datos, entrenar un modelo y predecir el comportamiento de un nuevo ingreso")

st.header("Quieres conocer como te iría a vos?")

model = joblib.load("modelo_entrenado.joblib")

def main():
    with st.form("inbox_form"):
        Married = st.selectbox("Se encuentra casado/a?",("Yes", "No"))
        Education = st.selectbox("Posee carrera de grado terminada?",("Graduate", "Not Graduate"))
        Self_Employed = st.selectbox("Posee trabajo independiente?",("Yes", "No"))
        ApplicantIncome = st.slider('Ingreso del Solicitante', 0, 41667, 1)
        CoapplicantIncome = st.slider('Ingreso del Co Solicitante', 0, 41667, 1)
        LoanAmount = st.slider('Monto del Préstamo', 9, 700, 1)
        Loan_Amount_Term = st.slider('Plazo del Préstamo', 12, 480, 1)
        Credit_History = st.selectbox("Posee historial crediticio?",("Yes", "No"))
        PropertyArea =st.selectbox("En que tipo de zona vive?",("Rural", "Semiurbana", "Urbana"))

        submit = st.form_submit_button("Predict")



    if submit:
        print("Las elecciones son:",Married, Education, Self_Employed)

        list = []
        Married_Yes = []    
        if Married == "Yes":
            Married_Yes = True
        else:
            Married_Yes = False
        
        Education_Not_Graduate = []
        if Education == "Yes":
            Education_Not_Graduate = False
        else:
            Education_Not_Graduate = True

        Self_Employed_Yes = []
        if Self_Employed == 'Yes':
            Self_Employed_Yes = True
        else:
            Self_Employed_Yes = False

        Property_Area_Urban = []
        if PropertyArea == "Urban":
            Property_Area_Urban = True
        else:
            Property_Area_Urban = False

        Property_Area_Semiurban = []
        if PropertyArea == "Semiurban":
            Property_Area_Semiurban = True
        else:
            Property_Area_Semiurban = False

        Credit_History_Yes = []
        if Credit_History == "Yes":
            Credit_History_Yes = True
        else:
            Credit_History_Yes = False

        ApplicantIncome2 = ApplicantIncomeStandard(ApplicantIncome)
        CoapplicantIncome = CoapplicantIncomeStandard(CoapplicantIncome)
        LoanAmount = LoanAmountStandard(LoanAmount)
        Loan_Amount_Term = Loan_Amount_TermStandard(Loan_Amount_Term)
        print("calculos intermedios", ApplicantIncome2,CoapplicantIncome, LoanAmount,
        Loan_Amount_Term)

        list = [ApplicantIncome2, CoapplicantIncome,LoanAmount, Loan_Amount_Term, Credit_History_Yes, Married_Yes, Education_Not_Graduate, Self_Employed_Yes,Property_Area_Semiurban, Property_Area_Urban]

        #array = np.array(ApplicantIncome, CoapplicantIncome,LoanAmount, Loan_Amount_Term, Credit_History, Married_Yes, Education_Not_Graduate, Self_Employed_Yes,Property_Area_Semiurban, Property_Area_Urban)
        
        print("este es el (pandas)", list)

        #print("este es el (numpy)", array)

        predict = model.predict([list])

        if predict == 1:
            st.header("Según el modelo, el / la prospecto abonaría su préstamo :moneybag: :tada:")
        else:
            st.header("Según el modelo, el / la usuario tendría problemas para devolver el préstamo :thumbsdown: :confused:")



st.write('Se aplico análisis, limpieza y tratamiento a los datos y luego diversos modelos de predicción; el modelo que brindo el mejor F1 Score fue DecissionTreeClassifier con un score de 87,67 %.')

st.subheader('No nos responsabilizamos por el otorgamiento de préstamo bajo el presente modelo :relieved:')

st.sidebar.markdown("# App")

def author():
    with st.sidebar:
        st.write("Hecho en las :mountain: ")

author()

if __name__ == '__main__':
    main()