import pickle
import streamlit as st
import pandas as pd
import math

#load model
with open('penduduk.pkl', 'rb') as fileP:
    loaded_penduduk = pickle.load(fileP)

def p_predict_data(input_data):
        pred_p = loaded_penduduk.predict(input_data)
        pred_roundedp = math.floor(pred_p)
        st.write(f'Prediksi Jumlah Penduduk Terpapar Terdampak Bencana Abrasi: {pred_roundedp} jiwa')

if __name__ == '__main__':
    p_predict_data()