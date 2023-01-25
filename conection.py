import mysql.connector
import streamlit as st
def init_connection():
   
    #return mysql.connector.connect(**st.secrets.mysql)
    return mysql.connector.connect(
     host="eu-central.connect.psdb.cloud",
     database="mexicodb",
     user="tw5ho6uhf9ahj6khhnsw",
    password="pscale_pw_NFeAGIeeHU64TkKYeadWGfT9Hnp4Tj2clH3U4O1ZuEW"
     )
    
