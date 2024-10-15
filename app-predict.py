import streamlit as st
import l_predict
import p_predict
import pandas as pd

def main():
    st.title('Aplikasi Prediksi Dampak Abrasi: Luasan dan Populasi Terpapar')
    st.write('Aplikasi ini memanfaatkan teknologi pembelajaran mesin untuk memprediksi persentase luasan wilayah dan jumlah penduduk yang terpapar bencana abrasi. Dengan memasukkan data geografis dan demografis, aplikasi ini memberikan proyeksi untuk membantu pengambilan keputusan terkait mitigasi bencana dan perencanaan wilayah pesisir.')
    menu = ['Home','Predict']
    choice = st.sidebar.selectbox('Menu', menu)

    if choice == 'Home':
        st.title('Selamat Datang di Aplikasi Prediksi Bencana Abrasi')
    else :
        st.title('Prediksi Presentase Luasan & Penduduk Terpapar Bencana Abrasi di Kabupaten Sambas')

        luas = st.number_input('Luas Wilayah (Km2)')
        jarak = st.number_input('Jarak ke Ibu Kota Kabupaten (km)')
        jumlah_p = st.number_input('Jumlah Penduduk')
        padat_p = st.number_input('Kepadatan Penduduk')
        perempuan = st.number_input('Perempuan')
        lansia = st.number_input('Usia Lansia (60 ke atas)')
        anak = st.number_input('Usia Anak (0-14 tahun)')
        hamil = st.number_input('Ibu Hamil')
        pendidikan = st.number_input('Tingkat Pendidikan (SMA/sederajat)')
        
        input_data = pd.DataFrame({
        'Luas Wilayah (Km2)': [luas],
        'Jarak ke Ibu Kota Kabupaten (km)' : [jarak],
        'Jumlah Penduduk' : [jumlah_p],
        'Kepadatan Penduduk': [padat_p],
        'Perempuan': [perempuan],
        'Usia Lansia (60 ke atas)': [lansia],
        'Usia Anak (0-14 tahun)': [anak],
        'Ibu Hamil': [hamil],
        'Tingkat Pendidikan (SMA/sederajat)': [pendidikan],
        })
        if st.button('Prediksi'):
            l_predict.l_predict_data(input_data)
            p_predict.p_predict_data(input_data)

if __name__ == '__main__':
    main()
