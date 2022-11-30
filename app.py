# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 19:13:49 2022

@author: anany
"""


import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json() 

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_ybiszbil.json")   


# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Ananya :wave:")
    st.title("Addition of 2 Numbers")
    st.write(
        "Week 8 Graded Assignment."
    )
    
    
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        n1 = st.number_input("Enter the first number")
         
        
        n2 = st.number_input("Enter the second number")
        try:
            sum = n1+n2
        except:
            st.text("Enter the second number")
        # check if the button is pressed or not
        if(st.button('Calculate SUM')):
            
            # print the BMI INDEX
            st.text("The sum of numbers is {}.".format(sum))
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")




 

 
    