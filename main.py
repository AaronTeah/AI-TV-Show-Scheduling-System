import streamlit as st

#streamlit header setting
st.header("TV Show Scheduling System", divider="gray") 

#customize input for crossover rate and mutation rate
CO_R = st.number_input(
    "Enter your Crossover Rate",
    min_value=0.00,
    max_value=0.95)
MUT_R = st.number_input(
    "Enter your Mutation Rate", 
    min_value=0.01,
    max_value=0.05) 

st.write("Crossover Rate: ", CO_R)
st.write("Mutation Rate: ", MUT_R) 
#st.dataframe() 


