from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

st.beta_set_page_config(layout="wide")
"""
# Financial Calculations

"""

# Annual Time Value of Money

st.sidebar.header("Select Chapter")

chapter = st.sidebar.radio("Select Chapter", ('Finance', 'Economics', 'Statistics'))

if chapter == 'Finance':
    option_finance = st.selectbox('Select Topic',('Annual Time Value of Money', 'Sub-Annual Time Value of Money', 'Constant Annuity & Perpetuity'))
    if option_finance == 'Annual Time Value of Money':
        st.header("Calculate Future Values")
        st.write("Example : You have $50,000 in savings for retirement. If your investments earn 7% annually, how much will you accumulate in 40 years?")
        presentValue1 = st.number_input('Input Present Value')
        interestAnnulay1 = st.number_input('Input Interest rate, like .07 etc')
        years1 = st.number_input('Input Years')
        st.write("Future Value")
        
        if st.button("Calculate Future Value"):
            futureValue = presentValue1*(1 + interestAnnulay1)** years1
            st.write(futureValue)



        st.header("Calculate Present Values")
        st.write("Example : What is the value today of $50,000 to be received twenty years from now if the appropriate interest rate is 6%?")
        finaltValue2 = st.number_input('Input Future Value')
        interestAnnulay2 = st.number_input('Input Interest rate, like .06 etc')
        years2 = st.number_input('Input Years here')
        st.write("Calculate Present Value")
        if st.button("Calculate Present Value"):
            futureValue2 = finaltValue2/(1+interestAnnulay2)**years2
            st.write(futureValue2)
            
            
            
        st.header("Calculate Rate")
        st.write("Example :A financial institution offers a double-your money savings account in which you receive $2 in fourteen years for every dollar you invest today. What annual interest rate does this account offer ?")
        presentValue3 = st.number_input('Input Present Value : ex 3')
        finalValue3 = st.number_input('Input Final Value like 60000 etc')
        years3 = st.number_input('Input Years here : Ex 3')   
        st.write("Calculate Rate")
        if st.button("Calculate Rate"):
            rate3 = (finalValue3/presentValue3)**(1/years3) -1
            st.write(rate3)


