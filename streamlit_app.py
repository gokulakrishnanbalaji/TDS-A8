

import streamlit as st

def compute_max(a,b,c):
    l=list([a,b,c])
    return max(l)

a= st.number_input("Enter the first number",step=1)
b= st.number_input("Enter the second number",step=1)
c= st.number_input("Enter the third number",step=1)

m=compute_max(a,b,c)
st.write("Max = ",m)

