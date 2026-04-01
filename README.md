Global Petrol Price Dashboard (2020-2026)

This interactive dashboard analyzes global fuel price trends, regional distributions, and the economic impact of subsidies across 2020 to 2026.

Project Structure
app.py: The main Python script containing the Streamlit and Plotly logic.
data_preparation.py: Script for data cleaning, merging, and initial EDA.
country_petrol_2020_2026.csv: The primary dataset
crude_oil_2020_2026.csv: The secondary dataset

README.md: This instruction file.

Prerequisites
Before running the dashboard, ensure you have Python 3.x installed and the following libraries:

Bash
pip install streamlit pandas plotly
How to Run the Dashboard
Open VS Code and open the project folder.

Open a New Terminal in VS Code.

Type the following command and press Enter:

Bash
python -m streamlit run app.py
The dashboard will automatically open in your default web browser at http://localhost:8501.

Visualizations Included
Price Trends Over Time (Line Chart): Tracking volatility from 2020-2026.

Regional Price Distribution (Box Plot): Identifying statistical outliers by continent.

Global Price Map (Choropleth): Geospatial analysis of fuel affordability.

Avg Price per Region (Bar Chart): Direct comparison of mean costs.

Price Frequency (Histogram): Analysis of global price concentration.

Subsidy Impact (Violin Plot): Visualizing price density and government intervention.