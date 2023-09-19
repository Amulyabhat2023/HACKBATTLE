import streamlit as st

st.set_page_config(page_title="Ask your seniors", page_icon=":crown:", layout= "wide")

with st.container():
    st.subheader("Hello dear freshers, Welcome to VIT!")
    st.title("How can we help you?")
    cont= """<form action="https://formsubmit.co/vitvfreshie@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">  
     <input type="text" name="name" placeholder="NAME" required>
     <input type="text" name="Register Number" placeholder="Register Number" required>
     <input type="text" name=""Query" placeholder="Enter your query" required>
     <button type="submit">Submit</button>
</form>
"""

lf, rt= st.columns(2)
with lf:
    st.markdown(cont, unsafe_allow_html=True)
with rt:
    st.empty()

