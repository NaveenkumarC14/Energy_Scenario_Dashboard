import streamlit as st
import pandas as pd
your_name = st.text_input("Number")
df=pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vR0UpG1xhHKc8BVAFyGr-e8PPlwnwY0_7I7KXx0AxL1s3V3StO4YVA8mRnACBE7FyFXD9HPMqI4yh7r/pub?gid=0&single=true&output=csv')
al=your_name in df['phone']
print('al')