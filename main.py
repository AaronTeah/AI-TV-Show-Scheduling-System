import streamlit as st
st.set_page_config(
  page_title="TV Show Scheduling System"
)

st.header("TV Show Scheduling System", divider="gray") 

age = st.slider("How old are you?", 0, 130, 25)
st.write("I'm ", age, "years old")
