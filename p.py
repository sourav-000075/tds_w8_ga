import streamlit as st
import numpy as np
import pandas as pd

st.title('Adding 2 numbers')
def user_input():
    n1 = st.number_input("n1")
    n2 = st.number_input("n2")
    data={
        'n1':n1,
        'n2':n2
    }
    features = pd.DataFrame(data, index=[0])
    return features,n1,n2

df,n1,n2 = user_input()

st.subheader('User Input parameters')
st.write(df.to_dict())
st.subheader('Sum:')
st.write(int(n1+n2))
