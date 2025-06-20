
import streamlit as st
st.title("navigation")

# nav=st.navigation(["page1.py","page2.py"])
# nav.run()
contact=st.navigation(["Home.py","Contact.py","page1.py","page2.py"])
contact.run()