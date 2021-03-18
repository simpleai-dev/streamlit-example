from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np

st.beta_set_page_config(layout="wide")
"""
# Financial Calculations

"""

# Annual Time Value of Money

st.sidebar.header("Select Chapter")

chapter = st.sidebar.radio("Select Chapter", ('Finance', 'Economics', 'Statistics'))

if chapter == 'Finance':
    option_finance = st.selectbox('Select Topic',('Annual Time Value of Money', 'Constant Annuity & Perpetuity'))
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

        st.header("Number of Years")
        st.write("Example : You have $50,000 in savings for retirement in an investment earning 7% annually. You aspire to have $1 million in savings when you retire. Assuming you add no more to your  savings, how many years will it take to reach your $1 million goal.")
        NY_present_value = st.number_input("4.1: Input Present Value")
        NY_rate = st.number_input("4.2: Input value of rate ")
        NY_final_value = st.number_input("4.3: Input Final Value ")
        st.write("4: Calculate Number of years")
        if st.button("4: Calculate Number of Years "):
            NY_result = round(np.log(NY_final_value/NY_present_value)/np.log(1+NY_rate),2)
            st.write(NY_result)
            
            
    if option_finance == 'Constant Annuity & Perpetuity':
        
        st.write("Consider an account holding $10000 and earning 10% interest each year")
        st.write("a. How much interest would be due at the end of one year ? ")
        CAP_PV = st.number_input("CAP : Enter Present Value")
        CAP_R = st.number_input("CAP: Enter Rate ")
        if st.button("CAP: calculate Payment"):
            CAP_PMT = CAP_PV * CAP_R
            st.write("Total Interest Due : ")
            st.write(CAP_PMT)
        st.write("b. If the account holder withdraws the first years's interest, how much interest would be due at the end of the second year ? ")
        st.write("Answer: Again 1000")
        st.write("c. Is teher any reason this process could not continue indefinitely?")
        st.write("Ans : No reason, it can keep going forever.")
        st.write("A student borrows $75,000 for bussiness scholl at 6.5% stated annual interest with repayments for 10 years. No additional interest accrues before the first payment.")
        st.write("a. How much is the monthly Payment?")
        st.write("b. What is the sum of all the payments ? ")
        st.write("c. What is the total interest Paid ? ")
        st.subheader("Annuity(Fixities)")
        st.write("An annuity is a periodic payment for a fixed term")
        st.write("A constant annuity is an annuity with a constant periodic payment.")
        st.subheader("Perpetuity")
        st.write("A perpetuity is a periodic payment forever.")
        st.write("A constant perpetuity is a perpetuity with a constant periodic payment.")
        st.subheader("Constant Perpetuity")
        st.write("What is the present value today of $3000 paid each year forever, assuming a discount rate of 5% and the first payment is received one year from now?")
        st.subheader('OR')
        st.write("What amount would you have to invest today at 5% annual interest to generate an annual payment of $3000 forever ?")
        CAP_PMT_2 = st.number_input("CAP 2: Enter Payment amount")
        CAP_R_2 = st.number_input("CAP 2: Enter Rate")
        if st.button("CAP2 : Calculate Present Value PV "):
            CAP_PV_2 = CAP_PMT_2/CAP_R_2
            st.write("So you need to invest : ")
            st.write(CAP_PV_2)
        
        
        
        
        