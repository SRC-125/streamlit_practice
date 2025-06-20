
import streamlit as st
 
st.title("Streamlit Session State")
 
first_name = st.text_input("First Name")
last_name = st.text_input("Last Name")
 
if "complete_name" not in st.session_state:
    st.session_state.complete_name = ""
 
 
if first_name and last_name:
    st.session_state.complete_name = first_name+last_name

# st.text(st.session_state.complete_name)
if st.button("View Details"):
    st.write(f"Hello {st.session_state.complete_name}")
    st.text(st.session_state.complete_name)
   

    