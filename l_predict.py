import pickle
import streamlit as st
import pandas as pd

#load model
with open('luas.pkl', 'rb') as fileL:
    loaded_luas = pickle.load(fileL)

def l_predict_data(input_data):
    pred_l = loaded_luas.predict(input_data)
    pred_rounded = f"{pred_l[0]:.2f}"
    st.write(f'Prediksi Presentase Luas Daerah Terdampak Bencana Abrasi: {pred_rounded} %')
    if pred_l <= 1.5:
        st.write('Tingkat Kerentanan = Rendah')
    elif pred_l > 1.5 and pred_l <= 4:
        st.write('Tingkat Kerentanan = Sedang')
    else:
        st.write('Tingkat Kerentanan = Tinggi')

if __name__ == '__main__':
    l_predict_data()