import langchain_helper as lch
import streamlit as st

st.title("Pets name Generator")

user_animal_type = st.sidebar.selectbox("What is your pet",("Cat", "Dog", "Cow","Hamster"))


user_pet_color = st.sidebar.text_input(label=f"What color is your {user_animal_type}",max_chars=15)

#response = lch.generate_pet_name(user_animal_type,user_pet_color)

#st.text(response["pet_name"])