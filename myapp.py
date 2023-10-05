import streamlit as st
import pandas as pd
import numpy as np

chart_data = pd.read_csv('counts.csv')

st.bar_chart(chart_data, columns=['dia3','dia4','dia5'], x='device_id')

