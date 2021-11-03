
import streamlit as st
import pandas as pd
import sqlite3

con = sqlite3.connect('modelorama.db')
cur = con.cursor()

st.set_page_config(page_title='Modelorama El Rodeo', page_icon='🍻')

# Header
# (pendiente)

# Sidebar
sidebar = st.sidebar
sidebar.image('logoModelorama.png')
menu_principal = sidebar.selectbox('', ['Principal', 'Indicadores', 'Ingresos', 'Gastos', 'Inventarios', 'Pedidos'])
sidebar.markdown('___')

menu_pos = sidebar.selectbox('POS', ['Punto de venta','Arqueo de efectivo'])
sidebar.markdown('___')

menu_catalogos = sidebar.selectbox('Catálogos', ['Productos', 'Empleados', 'Clientes', 'Proveedores', 'Categorías de ingresos', 'Categorías de gastos', 'Formas de pago'])


# Menú catálogos: Formas de pago

if menu_catalogos == 'Formas de pago':
    
    df_formas_pago = pd.read_sql('SELECT * FROM cat_formas_pago', con)
    df_formas_pago = df_formas_pago.sort_values(by='clave', ascending=False).set_index('clave')
    
    col1, col2 = st.columns((1,2))
    with col1:
        st.subheader('Alta de forma de pago')
        form = st.form('Forma de pago', clear_on_submit=True)
        descripcion = form.text_input('Descripcion:','')    
        form_submit = form.form_submit_button('Agregar')
    
        if form_submit:
            cur.execute("insert into cat_formas_pago (descripcion) values (?)", (descripcion,))
            con.commit()
            con.close()
    with col2:
        #st.table(df_forma_pago)
        st.table(df_formas_pago)
