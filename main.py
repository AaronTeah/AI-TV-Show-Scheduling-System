import streamlit as st
st.set_page_config(
  page_title="TV Show Scheduling System"
)

st.header("TV Show Scheduling System", divider="gray") 

age = st.slider("How old are you?", 0, 1, 0)
st.write("I'm ", age, "years old")
