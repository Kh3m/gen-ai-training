import streamlit as st
import pandas as pd
import numpy as np

st.title("Love To Code")


st.write("Pandas DataFrames",)

df = pd.DataFrame([
    [1,2,3,4,5],
    [6,7,8,9,10],
], columns=["A", "B", "C", "D", "E"])

people_df = pd.DataFrame({
    "Name": ["Abdulkareem", "Khem", "Adams"],
    "Age": [23,12, 32],
})

st.write(df)
st.write(people_df)

# Create a chart - line

data = np.random.randn(20, 3)
st.line_chart(data)