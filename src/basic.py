import streamlit as st

st.title(" ☕☕ List of coffees ☕☕ ")
type_of_coffee = st.selectbox("What type of coffee do you like?",["hot","iced"])
filtertitle = st.text_input("What do you like on top of your coffee?")

if filtertitle:
    st.text(f"😁 Oh! You like {type_of_coffee} Coffees with {filtertitle} on top")