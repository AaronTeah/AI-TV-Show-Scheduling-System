import streamlit as st
st.set_page_config(
  page_title="TV Show Scheduling System"
)

st.header("TV Show Scheduling System", divider="gray") 

CO_R = st.number_input(
    "Enter your Crossover Rate",
    min_value=0.00,
    max_value=0.95)
MUT_R = st.number_input(
    "Enter your Mutation Rate", 
    min_value=0.00,
    max_value=0.95) 

st.write("Crossover Rate: ", CO_R)
st.write("Mutation Rate: ", MUT_R)
