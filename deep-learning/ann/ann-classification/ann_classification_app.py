import streamlit as st
import pickle
from tensorflow.keras.models import load_model
import os
import pandas as pd

st.title("ANN Classification Problem")
st.header("Chrun Prediction", divider=True)

app_dir = os.path.dirname(__file__)

# Import models and encoders

@st.cache_resource
def load_artifacts():
    sequential_model = load_model(f"{app_dir}/sequential_model.keras")

    with open(f"{app_dir}/gender_label_encoder.pkl", "rb") as file:
        gender_label_encoder = pickle.load(file)
        
    with open(f"{app_dir}/geo_one_hot_encoder.pkl", "rb") as file:
        geo_one_hot_encoder = pickle.load(file)
        
    with open(f"{app_dir}/scaler.pkl", "rb") as file:
        scaler = pickle.load(file)
        
    return sequential_model, gender_label_encoder, geo_one_hot_encoder, scaler

sequential_model, gender_label_encoder, geo_one_hot_encoder, scaler = load_artifacts()

# Collect input data
input_data = {
    'CreditScore': st.number_input("Credit Score"),
    'Geography': st.selectbox("Geography", geo_one_hot_encoder.categories_[0]),
    'Gender': st.selectbox("Gender",gender_label_encoder.classes_),
    'Age': st.slider('Age', 18, 100),
    'Tenure':st.slider('Tenure', 0, 20),
    'Balance': st.number_input("Balance"),
    'NumOfProducts': st.slider("Number Of Products", 0, 4),
    'HasCrCard': st.selectbox("Has Credit Card", [0, 1]),
    'IsActiveMember': st.selectbox("Active Member", [0, 1]),
    'EstimatedSalary': st.number_input("Estimated Salary")
}

st.subheader("Raw Data")
input_df = pd.DataFrame([ input_data ])
st.write(input_data)
st.write(input_df)

st.subheader("Processed Data")
input_df["Gender"] = gender_label_encoder.transform([input_df["Gender"]])
geo_encoded = geo_one_hot_encoder.transform([ input_df["Geography"] ])
geo_encoded_df = pd.DataFrame(geo_encoded.toarray(), columns=geo_one_hot_encoder.get_feature_names_out())
input_df = pd.concat([ input_df.drop("Geography", axis=1), geo_encoded_df,  ], axis=1)
st.write(input_df)

st.subheader("Scaled Data")
scaled = scaler.transform(input_df)
st.write(scaled)

st.subheader("The Prediction")
prediction = sequential_model.predict(scaled)
prediction_proba = prediction[0][0]

st.markdown(f"""
    Churn Probability: **{prediction_proba:.2f}**
    
    {"**The customer is likely to churn.**" if prediction_proba > 0.5 else "**The customer is not likely to churn.**"}
""")