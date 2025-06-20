
import streamlit as st
# st.header("First streamlit page")
# st.title("Streamlit Sessions")
 
# st.header("This is my first Streamlit Page")
# st.subheader("Welcome to the first streamlit page")
 
# st.text("We are working on a Streamlit application")
st.header("App Structure")
 
# name = st.text_input("Enter your name:")
 
# age = st.slider("Select your age", 0, 100)
 
# # st.write(f"Hello {name}, you are {age} years old.")
# if st.checkbox("View Details"):
 
#     st.write(f"Hello {name}, you are {age} years old.")

with st.sidebar:
 
    st.write("Sidebar content here")
 
    col1, col2 = st.columns(2)
 
    col1.write("Left panel")
 
    col2.write("Right panel")