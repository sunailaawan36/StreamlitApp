# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 06:47:53 2022

@author: Sunaila Awan
"""

import streamlit as st
import pandas as pd

df = pd.read_csv('AirPassengers.csv')
df['Month'] = pd.to_datetime(df['Month'])
df['Year'] = df['Month'].apply(lambda x: x.year)

# def greet(name, gender):
#     if gender.lower()=='female':
#         greeting = 'Hello Ms.'+name.capitalize()
#     else:
#         greeting = 'Hello Mr.'+name.capitalize()
#     return greeting

def main():
    st.title('Air Passenger Analysis')
    yr = st.selectbox('Year', df['Year'].unique())
    table = df[df['Year']==yr]
    bt = st.button('Submit')
    if bt:
        st.table(table)
    # name = st.text_input('Name: ')
    # gender = st.selectbox('Gender:', ['Female','Male'])
    # button = st.button('Greet me!')
    # if button:
    #     greeting = greet(name, gender)
    #     st.success(greeting)

if __name__=='__main__':
    main()

    
