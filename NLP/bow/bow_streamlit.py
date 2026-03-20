import re
import streamlit as st
import pandas as pd
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer

# Load Data
@st.cache_data
def load_data():
    return pd.read_csv("../datasets/smsspamcollection.csv")

# Clean Data
@st.cache_data
def process_messages(df):
    ps = PorterStemmer()
    stop_words = set(stopwords.words("english")) # Set is faster for lookups
    processed = []
    for i in range(len(df)):
        # Convert message to lower case
        lower_message = df["message"][i].lower()
        # Remove special characters from message
        message = re.sub("[^a-zA-Z]", " ", lower_message)
        # Tokenize message to words
        words = word_tokenize(message)
        # Remove stopwords and apply stem
        messages = [ ps.stem(w) for w in words if w not in stop_words ]
        # Convert array of words back to sentence (message)
        message = " ".join(messages)
        # Append result to processed array
        processed.append({"label": df["label"][i] , "message": message})
    
    return pd.DataFrame(processed)

# Vectorize Data
@st.cache_data
def create_bow(data_column):
    cv = CountVectorizer(max_features=100)
    bow_matrix = cv.fit_transform(data_column).toarray()
    # Return both the array and the words so we can label the columns
    return bow_matrix, cv.get_feature_names_out()

# Use the cached functions
sms_pd = load_data()
processed_pd = process_messages(sms_pd)
bow_array, words = create_bow(processed_pd["message"])

st.title("Let's Build Something Amazing with BOW")
st.write("This file will show us how data is being processed before passing it for vectorization")

st.subheader("Stopwords")
st.write(pd.DataFrame(stopwords.words("english"), columns=["Stopwords"]))

st.subheader("Before Processing SMS Spam Collection Dataset", )
st.write(sms_pd)

# Processing
st.markdown(
"""
### Processing Steps
1. lowercase rows
2. apply regex to remove special characters
3. tokenize sentence (row) to words
4. remove stopwords
5. get the words stem or lemma
"""
)

st.subheader("After Processing SMS Spam Collection Dataset", )
st.write(processed_pd)

st.subheader("Finally Vectorize - Create Bag Of Words", )
bow_df = pd.DataFrame(bow_array, columns=words)
st.write(bow_df)
