
import streamlit as st

st.header('Arqueo de Efectivo')
st.markdown('___')

col1, col2 = st.columns(2)

with col1:

    mercado_pago = st.number_input('Tarjetas-Cédito/Débito:', 0)
    st.text(' ')
    st.markdown('___')
    st.text(' ')
        
    b20 = st.number_input('Billetes de $20:', 0)
    b50 = st.number_input('Billetes de $50:', 0)
    b100 = st.number_input('Billetes de $100:', 0)
    b200 = st.number_input('Billetes de $200:', 0)
    b500 = st.number_input('Billetes de $500:', 0)
    b1000 = st.number_input('Billetes de $1000:', 0)

with col2:
    monedas_10c = st.number_input('Monedas de 10 cent.',0)
    monedas_20c = st.number_input('Monedas de 20 cent.',0)
    monedas_50c = st.number_input('Monedas de 50 cent.',0)
    monedas_1p = st.number_input('Monedas de 1 peso',0)
    monedas_2p = st.number_input('Monedas de 2 pesos',0)
    monedas_5p = st.number_input('Monedas de 5 pesos',0)
    monedas_10p = st.number_input('Monedas de 10 pesos',0)
    monedas_20p = st.number_input('Monedas de 20 pesos',0)

    total_monedas = monedas_10c*0.10 + monedas_20c*0.20 + monedas_50c*.50 + monedas_1p*1 + monedas_2p*2 + monedas_5p*5 + monedas_10p*10 + monedas_20p*20
    total_billetes = b20*20 + b50*50 +b100*100 + b200*200 + b500*500 + b1000*1000
    total = total_monedas + total_billetes + mercado_pago
    

st.markdown('___')
st.write('Tarjetas-Cédito/Débito: ', mercado_pago)
st.write('     Monedas: ', round((total_monedas),2))
st.write('    Billetes: ', total_billetes)
st.success(f'El importe total del arqueo es: {round((total),2)}')
