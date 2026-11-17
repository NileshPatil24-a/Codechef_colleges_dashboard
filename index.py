# pyrefly: ignore[missing-import]
import streamlit as st

st.title("Hello World 👋")

st.header("Welcome to Streamlit")

st.write("This is my first Streamlit UI!")

name = st.text_input("Enter your name")

if st.button("Submit"):
    st.success(f"Hello, {name}! 🎉")
