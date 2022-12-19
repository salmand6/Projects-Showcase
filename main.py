import streamlit as st

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("Ignacio Salmerón Andreu")
    content = """
    Estudiante de doble grado trabajador, ambicioso y con ganas de aprender. Me gusta trabajar para resolver problemas y 
    creo en el esfuerzo como la manera de alcanzar grandes objetivos en la vida. Aptitud para planificar, manejar la 
    presión y liderar proyectos. Ganas de avanzar y destacar en mi carrera. Auto-didacta y apasionado de Python.
    """
    st.info(content)