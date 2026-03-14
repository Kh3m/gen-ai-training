import streamlit as st

name = st.text_input("Enter your name: ")

if name:
    st.write("Your name is: ", name)