import streamlit as st
import pandas as pd

# Load the CSV file into a Pandas DataFrame
@st.cache
def load_data():
    df = pd.read_csv('counts.csv')
    return df

df = load_data()

# Set the page title
st.title("Bar Chart Example with Streamlit")

# Create a sidebar for user input (optional)
st.sidebar.header("Configuration")

# Select the column for x-axis (device_id)
x_axis_column = st.sidebar.selectbox("Select X-Axis Column:", df.columns, index=0)

# Select the columns for the bar chart
bar_columns = st.sidebar.multiselect("Select Bar Columns:", df.columns[1:], default=['dia3'])

# Create the bar chart using Streamlit
st.write(f"### Bar Chart - X-Axis: {x_axis_column}, Bars: {', '.join(bar_columns)}")

# Group by the selected x-axis column and calculate the sum of the selected bar columns
bar_data = df.groupby(x_axis_column)[bar_columns].sum()

# Plot the bar chart using Streamlit
st.bar_chart(bar_data)
