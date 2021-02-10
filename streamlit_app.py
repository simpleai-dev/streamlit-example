from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

st.beta_set_page_config(layout="wide")
"""
# Financial Calculations

"""


col1 , col2, col3 = st.beta_columns(3)





col1.header("Calculate Future Values")

col1.write("Example : You have $50,000 in savings for retirement. If your investments earn 7% annually, how much will you accumulate in 40 years?")



presentValue1 = col1.number_input('Input Present Value')

interestAnnulay1 = col1.number_input('Input Interest rate, like .07 etc')

years1 = col1.number_input('Input Years')

col1.write("Future Value")



if col1.button("Calculate Future Value"):
    futureValue = presentValue1*(1 + interestAnnulay1)** years1
    col1.write(futureValue)



col2.write("Calculate Present Values")

col2.write("Example : What is the value today of $50,000 to be received twenty years from now if the appropriate interest rate is 6%?")



finaltValue2 = col2.number_input('Input Future Value')

interestAnnulay2 = col2.number_input('Input Interest rate, like .06 etc')

years2 = col2.number_input('Input Years here')

col2.write("Calculate Present Value")



if col2.button("Calculate Present Value"):
    futureValue2 = finaltValue2/(1+interestAnnulay2)**years2
    col2.write(futureValue2)