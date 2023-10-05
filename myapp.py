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

# Set the page title
st.title("Line Chart Example with Streamlit")

# Create a sidebar for user input (optional)
st.sidebar.header("Configuration")

# Select the column for x-axis (device_id)
x_axis_column_line = st.sidebar.selectbox("Select X-Axis Column Line Chart:", df.columns, index=0)

# Select the columns for the line chart
line_columns_line = st.sidebar.multiselect("Select Line Columns Line Chart:", df.columns[1:], default=['dia3'])

# Create the line chart using Streamlit
st.write(f"### Line Chart - X-Axis: {x_axis_column_line}, Lines: {', '.join(line_columns_line)}")

# Group by the selected x-axis column and calculate the sum of the selected line columns
line_data = df.groupby(x_axis_column_line)[line_columns_line].sum()

# Plot the line chart using Streamlit
st.line_chart(line_data)
