import streamlit as st

# Title
st.title("🌟 My First Streamlit App")

# Header
st.header("Welcome to Streamlit!")

# Text
st.write("This is a simple demo app built with Streamlit in Python.")

# Input box
name = st.text_input("Enter your name:")

# Slider
age = st.slider("Select your age:", 1, 100, 20)

# Button
if st.button("Submit"):
    st.success(f"Hello {name}, you are {age} years old! 🎉")

# Display a chart
import pandas as pd
import numpy as np

data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["A", "B", "C"]
)

st.line_chart(data)
