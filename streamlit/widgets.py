import streamlit as st
import pandas as pd

name = st.text_input("Enter your name: ")

if name:
    st.write("Your name is: ", name)

price=st.slider("Enter price range: ", 0, 100, 50)

st.write("You entered: ", price)

options = ["Male", "Female"]
sex = st.selectbox("Select Gender: ", options)

st.write("Your Gender: ", sex)

upload_file = st.file_uploader("Choose a CSV file", type="csv")
 
if upload_file:
    uploaded_csv = pd.read_csv(upload_file)
    st.write("You Uploaded: ")
    st.write(uploaded_csv)


