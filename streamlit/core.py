import streamlit as st
import pandas as pd

st.title("Love To Code")
df = pd.DataFrame([
    [1,2,3,4,5],
    [6,7,8,9,10],
], columns=["A", "B", "C", "D", "E"])

st.write(df)