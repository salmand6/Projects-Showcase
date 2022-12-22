import streamlit as st

st.header("Contact Me")

with st.form(key="email:forms"):
    user_email = st.text_input("Your email address")
    message = st.text_area("Enter your Message")
    button = st.form_submit_button("Submit")

    if button:
        print("Hello")