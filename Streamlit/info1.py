import streamlit as st
import pandas as pd
import numpy as np

# App titile and description
st.title("My first streamlit app.")
st.write("THis is a simple app to demonstrate the basic functionalities of streamlit.")

# Interactive widgets in the sidebar
st.sidebar.header("User Input Features")

# Text Input
user_name = st.sidebar.text_input("WHat is your name ?", "Streamlit User")

# Slider
age = st.sidebar.slider("Select your age", 0, 100, 25)

# Selectbox
favorite_color = st.sidebar.selectbox("What is your fav color ?", ["Blue", "Red", "Green", "Yellow"])

# Main page content
st.header(f"Welcom, {user_name}")
st.write(f"You are {age} years old and your favorite color is {favorite_color}")

# Displaying Data
st.subheader("Here's some random data:")

# Create a simple DataFrame
data = pd.DataFrame(
    np.random.rand(10, 5),
    columns=('col %d' % i for i in range(5))
)

st.dataframe(data)

# Checkbox to show/hide content
if st.checkbox("Show raw data"):
    st.subheader("Raw Data")
    st.write(data)
    
# Button to trigger an action
if st.button("Say hello"):
    st.write("Hello there!")
else:
    st.write("Goodbye")