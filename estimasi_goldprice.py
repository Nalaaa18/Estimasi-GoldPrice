import pickle
import streamlit as st

model = pickle.load(open('estimasi_goldprice.sav', 'rb'))

st.title('Estimasi Harga Emas')

Date = st.number_input('Input Tanggal')
Open = st.number_input('Input Harga Pembukaan Emas')
High = st.number_input('Input Harga Emas Tertinggi')
Low = st.number_input('Input Harga Emas Terendah')
Chg = st.number_input('Input Harga Penutupan Emas')

predict = ''

if st.button('Estimasi Harga'):
    predict = model.predict(
        [[Date, Open, High, Low, Chg]]
    )
    st.write ('Estimasi harga Emas dalam Ponds : ', predict)
    st.write ('Estimasi harga Emas dalam IDR (Juta) :', predict*17000)