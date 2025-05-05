import streamlit as st
import pandas as pd
import plotly.express as px

# Sample car sales data (replace with your actual data or load from CSV)
data = {
    'Model': ['Sedan', 'SUV', 'Coupe', 'Sedan', 'SUV', 'Coupe', 'SUV'],
    'Color': ['Red', 'Blue', 'Red', 'Black', 'White', 'Black', 'Red'],
    'Size': ['Medium', 'Large', 'Small', 'Medium', 'Large', 'Small', 'Large'],
    'Units Sold': [150, 200, 90, 180, 220, 100, 250],
    'Revenue': [300000, 500000, 180000, 350000, 600000, 200000, 750000]
}

df = pd.DataFrame(data)

st.set_page_config(page_title="Car Sales Dashboard", layout="wide")

st.title("🚗 Car Sales Dashboard")

# Sidebar filters
st.sidebar.header("🔍 Filter Cars")
selected_model = st.sidebar.multiselect("Select Model", options=df["Model"].unique(), default=df["Model"].unique())
selected_color = st.sidebar.multiselect("Select Color", options=df["Color"].unique(), default=df["Color"].unique())
selected_size = st.sidebar.multiselect("Select Size", options=df["Size"].unique(), default=df["Size"].unique())

# Filter data
filtered_df = df[
    (df["Model"].isin(selected_model)) &
    (df["Color"].isin(selected_color)) &
    (df["Size"].isin(selected_size))
]

st.subheader("Filtered Car Sales Data")
st.dataframe(filtered_df, use_container_width=True)

# Bar chart of Units Sold
fig_units = px.bar(
    filtered_df,
    x="Model",
    y="Units Sold",
    color="Color",
    title="Units Sold by Model and Color",
    barmode="group"
)
st.plotly_chart(fig_units, use_container_width=True)

# Pie chart of Revenue by Size
fig_revenue = px.pie(
    filtered_df,
    values="Revenue",
    names="Size",
    title="Revenue Distribution by Car Size"
)
st.plotly_chart(fig_revenue, use_container_width=True)
