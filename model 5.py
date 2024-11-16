# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 11:44:27 2024

@author: moksh
"""

import streamlit as st
import pickle


load = open('model5.pkl','rb')
model = pickle.load(load)

def predict(age,sex,albumin,alkaline_phosphatase,
       alanine_aminotransferase,aspartate_aminotransferase,bilirubin,
       cholinesterase,cholesterol,creatinina,
       gamma_glutamyl_transferase,protein):
    prediction = model.predict([[age,sex,albumin,alkaline_phosphatase,
           alanine_aminotransferase,aspartate_aminotransferase,bilirubin,
           cholinesterase,cholesterol,creatinina,
           gamma_glutamyl_transferase,protein]])
    return prediction\
        
        
def main():
    st.title("disease prediction ")
    
    age = st.number_input("Ages:")
    sex = st.number_input("Sex:")
    albumin = st.number_input("Albumin:")
    alkaline_phosphatase= st.number_input("Alkaline_phosphatase:")
    alanine_aminotransferase= st.number_input("Alanine_aminotransferase,:")
    aspartate_aminotransferase= st.number_input("Aspartate_aminotransferase:")
    bilirubin = st.number_input("Bilirubin:")
    cholinesterase= st.number_input("Cholinesterase:")
    cholesterol = st.number_input("Cholesterol:")
    creatinina = st.number_input("Creatinina:")
    gamma_glutamyl_transferase = st.number_input("Gamma_glutamyl_transferase:")  
    protein = st.number_input("Protein:")
    
    if st.button("predict"):
        result = predict(age,sex,albumin,alkaline_phosphatase,
               alanine_aminotransferase,aspartate_aminotransferase,bilirubin,
               cholinesterase,cholesterol,creatinina,
               gamma_glutamyl_transferase,protein)
        if result==0:
            st.success('cirrhosis')
        elif result==1:
            st.success('suspect_disease')
        elif result==2:
            st.success('fibrosis')
        else:
            st.success('no_disease')
            
            
            
            
if __name__ == '__main__':
    main()

    
