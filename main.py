import streamlit as st
import csv

############ Function to read the CSV file and convert it to the desired format######################
def read_csv_to_dict(file_path):
    program_ratings = {}
    
    with open(file_path, mode='r', newline='') as file:
        reader = csv.reader(file)
        # Skip the header
        header = next(reader)
        
        for row in reader:
            program = row[0]
            ratings = [float(x) for x in row[1:]]  # Convert the ratings to floats
            program_ratings[program] = ratings
    
    return program_ratings

# Path to the CSV file
file_path = 'program_ratings.csv'

# Get the data in the required format
program_ratings_dict = read_csv_to_dict(file_path)

# Print the result (you can also return or process it further)
for program, ratings in program_ratings_dict.items():
    print(f"'{program}': {ratings},")

import random

##################################### DEFINING PARAMETERS AND DATASET ################################################################
# Sample rating programs dataset for each time slot.
ratings = program_ratings_dict

GEN = 100
POP = 50
CO_R = 0.8
MUT_R = 0.2
EL_S = 2

all_programs = list(ratings.keys()) # all programs
all_time_slots = list(range(6, 24)) # time slots
st.set_page_config(
  page_title="TV Show Scheduling System"
)

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

