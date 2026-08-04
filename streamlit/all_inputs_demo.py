import streamlit as st
import pandas as pd
import datetime

st.title("Streamlit Input Widgets - Full Demo")
st.caption("Every input widget in one place")

# ---------------- TEXT / NUMBER ----------------
st.header("Text & Number Inputs", divider="red")

text_val = st.text_input("Text input", placeholder="Type something")
area_val = st.text_area("Text area", placeholder="Type a longer message")
num_val = st.number_input("Number input", min_value=0, max_value=100, value=10, step=1)

st.write("Values:", text_val, area_val, num_val)

# ---------------- SELECTION ----------------
st.header("Selection Widgets", divider="red")

select_val = st.selectbox("Selectbox", ["Option A", "Option B", "Option C"])
multi_val = st.multiselect("Multiselect", ["Python", "SQL", "n8n", "LangChain"], default=["Python"])
radio_val = st.radio("Radio buttons", ["Yes", "No", "Maybe"])
check_val = st.checkbox("Checkbox - I agree")
toggle_val = st.toggle("Toggle switch")
slider_select_val = st.select_slider("Select slider", options=["Low", "Medium", "High"])

st.write("Values:", select_val, multi_val, radio_val, check_val, toggle_val, slider_select_val)

# ---------------- NUMERIC RANGE ----------------
st.header("Sliders", divider="red")

slider_val = st.slider("Number slider", 0, 100, 50)
range_val = st.slider("Range slider", 0, 100, (25, 75))

st.write("Values:", slider_val, range_val)

# ---------------- DATE / TIME ----------------
st.header("Date & Time Inputs", divider="red")

date_val = st.date_input("Date input", datetime.date.today())
time_val = st.time_input("Time input", datetime.time(9, 0))

st.write("Values:", date_val, time_val)

# ---------------- BUTTONS ----------------
st.header("Buttons", divider="red")

if st.button("Simple button"):
    st.write("Button clicked!")

st.download_button("Download button", data="Sample text content", file_name="sample.txt")
st.link_button("Link button", url="https://streamlit.io")

# ---------------- FILE / MEDIA ----------------
st.header("File & Media Inputs", divider="red")

uploaded_file = st.file_uploader("File uploader", type=["csv", "txt", "pdf"])
camera_photo = st.camera_input("Camera input")
audio_val = st.audio_input("Audio input")

if uploaded_file:
    st.write("Uploaded:", uploaded_file.name)

# ---------------- OTHER ----------------
st.header("Other Widgets", divider="red")

color_val = st.color_picker("Color picker", "#f43334")

data_editor_val = st.data_editor(
    pd.DataFrame({"Name": ["Item 1", "Item 2"], "Qty": [1, 2]}),
    num_rows="dynamic",
)

feedback_val = st.feedback("thumbs")
pills_val = st.pills("Pills selection", ["Tag 1", "Tag 2", "Tag 3"])

st.write("Color:", color_val)
st.write("Feedback:", feedback_val)
st.write("Pills:", pills_val)

# ---------------- FORM EXAMPLE ----------------
st.header("Grouped Inputs (Form)", divider="red")

with st.form("demo_form"):
    f_name = st.text_input("Name")
    f_age = st.number_input("Age", min_value=0, max_value=120)
    f_submit = st.form_submit_button("Submit form")

if f_submit:
    st.success(f"Form submitted: {f_name}, {f_age} years old")