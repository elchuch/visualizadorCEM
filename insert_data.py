import streamlit as st
import mysql.connector
def insert_data(c,x,y,cp,esc,estado,mun,col,calle,desc):
    cursor=c.cursor()
    escaped_x=c._cmysql.escape_string(x)
    escaped_y=c._cmysql.escape_string(y)
    escaped_cp=c._cmysql.escape_string(cp)
    escaped_esc=c._cmysql.escape_string(esc)
    escaped_estado=c._cmysql.escape_string(estado)
    escaped_mun=c._cmysql.escape_string(mun)
    escaped_col=c._cmysql.escape_string(col)
    escaped_calle=c._cmysql.escape_string(calle)
    escaped_desc=c._cmysql.escape_string(desc)
    


    cursor.execute("INSERT INTO ubicacion(coordenadaX,coordenadaY,cp,nombre_esc,estado,munDe,colonia,calleN,descripcion) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
     (escaped_x,escaped_y,escaped_cp,escaped_esc,escaped_estado,escaped_mun,escaped_col,escaped_calle,escaped_desc))
    c.commit()
    c.close()
    st.success("enviado correctamente")
       




 