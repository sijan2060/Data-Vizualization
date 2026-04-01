import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Load Data (Updated for VS Code local path)
df = pd.read_csv('country_petrol_2020_2026.csv')
df['Date'] = pd.to_datetime(df['Date'])

# 2. Page Setup
st.set_page_config(page_title="Global Petrol Price Dashboard", layout="wide")
st.title("Global Petrol Price Dashboard (2020-2026)")

# 3. Stable Filter
st.markdown("### Select Region to Focus")
# Using 'All' + unique regions for a better user experience
all_regions = ['All'] + sorted(list(df['Region'].unique()))
selected_region = st.radio("Choose a Region:", options=all_regions, horizontal=True)

if selected_region == 'All':
    df_selection = df
else:
    df_selection = df[df['Region'] == selected_region]

# 4. KPIs
c1, c2, c3 = st.columns(3)
c1.metric("Avg Petrol Price", f"${df_selection['Petrol_USD'].mean():.2f}")
c2.metric("Max Price", f"${df_selection['Petrol_USD'].max():.2f}")
c3.metric("Records Found", len(df_selection))

# 5. SIX CHART LAYOUT
row1_col1, row1_col2 = st.columns(2)
row2_col1, row2_col2 = st.columns(2)
row3_col1, row3_col2 = st.columns(2)

with row1_col1:
    st.subheader("1. Price Trends Over Time")
    st.plotly_chart(px.line(df_selection, x='Date', y='Petrol_USD', color='Country', template="plotly_dark"), use_container_width=True)

with row1_col2:
    st.subheader("2. Regional Price Distribution")
    st.plotly_chart(px.box(df_selection, x='Region', y='Petrol_USD', color='Region', template="plotly_dark"), use_container_width=True)

with row2_col1:
    st.subheader("3. Global Price Map")
    st.plotly_chart(px.choropleth(df_selection, locations="ISO", color="Petrol_USD", hover_name="Country", color_continuous_scale="Viridis"), use_container_width=True)

with row2_col2:
    st.subheader("4. Avg Price per Region")
    avg_region = df_selection.groupby('Region')['Petrol_USD'].mean().reset_index()
    st.plotly_chart(px.bar(avg_region, x='Region', y='Petrol_USD', color='Region', template="plotly_dark"), use_container_width=True)

with row3_col1:
    st.subheader("5. Price Frequency (Histogram)")
    st.plotly_chart(px.histogram(df_selection, x='Petrol_USD', nbins=30, color_discrete_sequence=['teal'], template="plotly_dark"), use_container_width=True)

with row3_col2:
    st.subheader("6. Subsidy Impact")
    st.plotly_chart(px.violin(df_selection, x='Subsidy', y='Petrol_USD', color='Subsidy', box=True, template="plotly_dark"), use_container_width=True)