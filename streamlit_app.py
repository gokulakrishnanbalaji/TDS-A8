

import streamlit as st

def compute_max(a,b,c):
    l=list([a,b,c])
    return max(l)

a= st.number_input("Enter the first number")
b= st.number_input("Enter the second number")
c= st.number_input("Enter the third number")

m=compute_max(a,b,c)
st.write("Max = ",m)

