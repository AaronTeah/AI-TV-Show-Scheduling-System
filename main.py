import streamlit as st
st.set_page_config(
  page_title="TV Show Scheduling System"
)

st.header("TV Show Scheduling System", divider="gray") 

x = st.slider("Crossover Rate", 0, 0.95, 25)
st.write("x = ", x)
