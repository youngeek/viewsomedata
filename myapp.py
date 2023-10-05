import streamlit as st
import pandas as pd
import numpy as np

chart_data = pd.read_csv('counts.csv')

st.bar_chart(chart_data)

