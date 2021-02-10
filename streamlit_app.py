from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Financial Calculations

"""

st.write("Calculate Future Values")

st.write("Example : You have $50,000 in savings for retirement. If your investments earn 7% annually, how much will you accumulate in 40 years?")



presentValue1 = st.number_input('Input Present Value')

interestAnnulay1 = st.number_input('Input Interest rate, like .07 etc')

years1 = st.number_input('Input Years')

st.write("Future Value")



if st.button("Calculate Future Value"):
    futureValue = presentValue1*(1 + interestAnnulay1)** years1
    st.write(futureValue)



st.write("Calculate Present Values")

st.write("Example : What is the value today of $50,000 to be received twenty years from now if the appropriate interest rate is 6%?")



finaltValue2 = st.number_input('Input Present Value')

interestAnnulay2 = st.number_input('Input Interest rate, like .07 etc')

years2 = st.number_input('Input Years')

st.write("Calculate Present Value")



if st.button("Calculate Present Value"):
    futureValue2 = finaltValue2/(1+interestAnnulay2)^years2
    st.write(futureValue2)