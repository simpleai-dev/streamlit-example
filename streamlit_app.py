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
    option_finance = st.selectbox('Select Topic',('Annual Time Value of Money', 'Constant Annuity & Perpetuity','Growing Annuity'))
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
            
            
        st.subheader("Constant Annuity Present Value")
        st.write("For tax reasons, your client wishes to purchase a 10-year annuity that pays $100000 each year, with the first payment in one year.")
        st.write("a: With no interest on the invested amount, how much would the client need to invest now?")
        st.write("Ans : 100000 multiply by 10")
        st.write("b: at 6% interest, how much would the client need to invest now? ")
        CAPV_n = st.number_input("CAPV: Enter number of years")
        CAPV_r = st.number_input("CAPV: Enter rate")
        CAPV_pmt = st.number_input("CAPV: Enter PMT")
        if st.button("CAPV: Calculate PV"):
            CAPV_PV = (CAPV_pmt/CAPV_r)*(1- 1/(1+CAPV_r)**CAPV_n)
            st.write(CAPV_PV)
            
        st.subheader("Constant Annuity Payment (Invest)or borrow")
        st.write("Suppose you invest $200000 in a 20-year constan annuity with the first payment one year from now.")
        st.write("b: At 7% rate of return, how much do you receive each year?")
        CAPI_PV = st.number_input("CAPV: Enter Present Value")
        CAPI_n = st.number_input("CAPI: Enter number of years")
        CAPI_r = st.number_input("CAPI: Enter rate")
        if st.button("CAPI: caluclate PMT "):
            CAPI_pmt = CAPI_PV*CAPI_r/(1-1/(1+CAPI_r)**CAPI_n)
            st.write(CAPI_pmt)
        st.write("c: At 7% rate of return, how much do you receive over 20 years ? ")
        st.write(" That will be  previous anser * 20 ")
        st.write("Total Interest = Total payment - PV")
        st.write("same will be valid for borrow")
        st.subheader("Constant Annuity Sub-Annual Payment")
        st.write("A student borrows $75000 for bussiness schoold at 6.5% stated annual interest with repayment in equal monthly payments for 10 years. No additional interest accurs during school.")
        st.write("a. How much is the monthly payment ? ")
        CASP_PV = st.number_input("CASP: Enter Present Value")
        CASP_rst = st.number_input("CASP: Enter Rate")
        CASP_n = st.number_input("CASP: Enter total years")
        CASP_p = st.number_input("CASP: Enter 12 if monthly")
        if st.button("CASP: Caluclate PMT"):
            CASP_PMT = CASP_PV*(CASP_rst/CASP_p)/(1-(1/(1+CASP_rst/CASP_p)**(CASP_n*CASP_p)))
            st.write(CASP_PMT)
        
        st.subheader("Constnat Annuity Sub-Annual Present Value")
        st.write("You can afford $300 per month for car loan payments.")
        st.write("a: For a 36-month loan at 6% stated annual interest, with the first payment one month from now, how much can you borrow?")
        st.write("b. What is the sum of the payments?")
        st.write("What is the total interest paid ?")
        CASPV_rst = st.number_input("CASPV: Enter Rate")
        CASPV_n = st.number_input("CASPV: Enter years 36-month = 3")
        CASPV_p = st.number_input("CASPV Enter P : monthyly = 12")
        CASPV_PMT = st.number_input("CASPV: Enter PMT")
        if st.button("CASPV : Caculate PV "):
            CASPV_PV = (CASPV_PMT/(CASPV_rst/CASPV_p))*(1-1/(1+CASPV_rst/CASPV_p)**(CASPV_n*CASPV_p))
            st.write(CASPV_PV)
            
    if option_finance == 'Growing Annuity':
        st.write("As we know that constant Perpetuity is PV=PMT/r")
        st.write("What amount would we have to put in the bank today at 5% annual interest to genereate a series of payments each year forever, starting with $1000 paid one year from now and the pament growing in each subsequent year by 2% to offfset inflation.")
        st.write("Formula : PV = PMT/(r-g)")
        GA1_PMT = st.number_input("GA1: Enter Payment")
        GA1_r = st.number_input("GA1: Enter Rate")
        GA1_g = st.number_input("GA1: Enter growth Rate")
        
        if st.button("GA1: Calculate PV "):
            GA1_PV = GA1_PMT/(GA1_r-GA1_g)
            st.write(GA1_PV)
        
        
        
        

        
        
        
        
        