import folium as f
import pandas as pd
import numpy as np
import seaborn as sns
import streamlit as st
from streamlit_folium import folium_static
import codecs
import streamlit.components.v1 as stc
import matplotlib.pyplot as plt
import conection
import insert_data as insert


 
c=conection.init_connection()

def openHtml(chtml, width=700, height=700):
    chtml = codecs.open(chtml, 'r')
    ohtml = chtml.read()
    stc.html(ohtml, width=width, height=height, scrolling=False)

def createMap(dataframe, condition, color, s):
    df = dataframe
    c = condition
    m = f.Map(location=[19.47851, -99.23963], zoom_start=10, tiles=s)
    for i in range(len(df.index)):
        if c == df['PROBLEMATICA'][i]:
            popup = f.Popup("<strong>Escuela:</strong>{}<br>\n<strong>Descripción:</strong>{}<br>\n<strong>Ageb:</strong>{}".format(
                df.ESCUELA[i], df['DESCRIPCION '][i], df.AGEB[i]), max_width=250)
            f.Circle(location=[df.X[i], df.Y[i]],
                     radius=50,
                     popup=popup,
                     color=color,
                     fill=True,
                     fill_opacity=0.9).add_to(m)
    return m


def showData(data):
    fig, ax = plt.subplots(figsize=(8, 2))
    sns.countplot(data=data, x='PROBLEMATICA', ax=ax)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=75)
    ax.set_xlabel("Problematicas")
    ax.set_ylabel("Cantidad")
    ax.set_title("Datos recabados por alumnos de FES-ACATLÁN")
    return fig
def convert_df(data):
    return data.to_csv().encode('utf-8')


def main():
    df = pd.read_csv("data/3333.csv")
    menu = ['Información', 'Mapa de denuncias']
    menuIn = ['Paso peatonal', 'Rampas', 'Vandalismo',
              'Seguridad', 'Luminarias', 'Señalización','Opciones']
    

    col6,col7=st.columns(2)
    col1, col2 = st.columns(2)
    with st.sidebar:
        st.image('images/logo1.jpeg', 'México social')
        choice = st.selectbox('Menu', menu)
    if choice == 'Mapa de denuncias':
        st.header("Denuncias  de FES-ACATLÁN")
        with col1:
            choice1 = st.selectbox('Selecciona', menuIn)
        with col2:
            choice2 = st.radio('Cambiar mosaico', options=[
                               'OpenStreetMap', 'cartodb positron'])
  
        
                              
      
        if choice1 == 'Paso peatonal':
            m1 = createMap(df, 'PASO PEATONAL', 'red', choice2)

            folium_static(m1, width=700, height=500)
        elif choice1 == 'Rampas':
            m2 = createMap(df, 'RAMPA', 'green', choice2)
            folium_static(m2, width=700, height=500)
        elif choice1 == 'Vandalismo':
            m3 = createMap(df, 'VANDALISMO', 'blue', choice2)
            folium_static(m3, width=700, height=500)
        elif choice1 == 'Seguridad':
            m4 = createMap(df, 'SEGURIDAD', 'black', choice2)
            folium_static(m4, width=700, height=500)
        elif choice1 == 'Luminarias':
            m5 = createMap(df, 'LUMINARIAS', 'black', choice2)
            folium_static(m5, width=700, height=500)
        elif choice1 == 'Señalización':
            m6 = createMap(df, 'SENALIZACION', 'black', choice2)
            folium_static(m6, width=700, height=500)
        elif choice1== 'Opciones':
            if st.checkbox("Mostrar csv",False):st.write(df)
            if st.checkbox("Mostrar grafica",False):st.write(showData(df))
            if st.download_button(label="Descargar csv",
            data=convert_df(df),
            file_name='dataMexSocial.csv',
            mime='text/csv' 

            ):st.markdown('DESCARGA EXITOSA')
            #st.write(API.api_get('restaurantes',21.85717833, -102.28487238,300))
        st.subheader("Realiza tu denuncia")
        col3,col4,col5=st.columns(3)
        st.write('Si no conoces las coordenadas y/o tampoco el codigo postal,puedes omitir estos campos')
        
        with col3:
            coorX = st.text_input("Ingresa coordenada x",placeholder='45.6776768')
         
        with col4:
            coorY = st.text_input("Ingresa coordenda y",placeholder='-99.678567')
          
        with col5:
            codigo_post = st.text_input("Ingresa tu codigo postal",placeholder='52600',max_chars=5)
           
        st.warning("Es obligatorio llenar los campos de abajo,  de lo contrario no se habilitara el boton enviar",icon="⚠️")
        nombre_esc=st.text_input('Ingresa nombre de la escuela',placeholder="Esc.Primaria Lic.Benito Juárez")
        estado=st.text_input('Ingresa nombre del Estado',placeholder="Michoacan",max_chars=30)
        municipio=st.text_input("Ingresa nombre del municipio o delegación",placeholder='Atlixco')
        colonia=st.text_input('Ingresa nombre de la colonia',placeholder='Tenextepec')
        calle=st.text_input("Nombre de la calle y numero",placeholder='Allende numero 10')
        descripcion=st.text_area('Descripcion del problema',placeholder='No se cuenta con alumbrado publico')
        if len(nombre_esc)==0 or len(estado)==0 or len(municipio)==0 or len(colonia)==0 or len(calle)==0 or len(descripcion)==0:
            st.error('faltan campos por llenar',icon="🚨")
        else:
            if  st.button("enviar reporte"):
                insert.insert_data(c,coorX,coorY,codigo_post,
                 nombre_esc,estado,municipio,colonia,calle,descripcion)
    
        

    
        
        



    else:
        openHtml("html/index.html")
        
    


if __name__ == '__main__':
    main()