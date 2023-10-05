import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a Pandas DataFrame
@st.cache
def load_data():
    df = pd.read_csv('data.csv')
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

# Create the bar chart
st.write(f"### Bar Chart - X-Axis: {x_axis_column}, Bars: {', '.join(bar_columns)}")

fig, ax = plt.subplots()
for col in bar_columns:
    ax.bar(df[x_axis_column], df[col], label=col)

# Set labels and title
ax.set_xlabel(x_axis_column)
ax.set_ylabel("Values")
ax.set_title("Bar Chart")
ax.legend()

# Display the chart using Streamlit
st.pyplot(fig)
