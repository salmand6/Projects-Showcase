import streamlit as st
import pandas as pd

col1, col2 = st.columns(2)


with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("Ignacio Salmerón Andreu")
    content = """
    Hola soy un estudiante de doble grado trabajador, ambicioso y con ganas de aprender. Me gusta trabajar para resolver 
    problemas y creo en el esfuerzo como la manera de alcanzar grandes objetivos en la vida. Aptitud para planificar, 
    manejar la presión y liderar proyectos. Auto-didacta y apasionado de Python.\n
    Hi! I'm an ambitious and eager to learn Law and Business student. I like to work to solve problems. I believe in 
    effort as the ultimate way of achieving big things in life. Apt to plan, handle pressure and lead the way. 
    In love with Python.
    """
    st.info(content)

content = """
Here you'll find some of the apps I've built in Python. Feel free to message me!
"""
text = st.write(content)

col3, col4 = st.columns(2)

df = pd.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:11].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[11:].iterrows():
        st.header(row["title"])