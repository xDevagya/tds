import streamlit as st

st.set_page_config(page_title="Largest Number App", page_icon=":bar_chart:")

st.header("Largest Number App")
st.write("A simple app to find the largest of three numbers. Made by 22f3001390(Devagya)")

with st.form(key="input_form"):
    n1 = st.number_input("Enter first number:", step=1)
    n2 = st.number_input("Enter second number:", step=1)
    n3 = st.number_input("Enter third number:", step=1)
    calc_button = st.form_submit_button("Find Largest Number")

if calc_button:
    largest_num = max(n1, n2, n3)
    st.success(f"The largest number is: {largest_num}")
