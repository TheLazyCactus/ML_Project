import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pickle  # Assuming the model is stored as a pickle file
from sklearn.preprocessing import OneHotEncoder

# URL of the data
url = 'https://raw.githubusercontent.com/TheLazyCactus/ML_Project/refs/heads/main/final_LTIR_predictions.csv'
df_final = pd.read_csv(url, sep=",", low_memory=False)

# Define a short list of companies
companies = df_final["Company"].unique()

# Dropdown to select a company
selected_company = st.selectbox("Select a Company:", companies)

# Load data for the selected company
company_data = df_final[df_final['Company'] == selected_company]

# Display predictions
st.write("### Predicted LTIR for the Next 3 Years")
st.dataframe(company_data)

# Plot trend for both historical and predicted LTIR

# Create a new DataFrame for plotting historical and predicted LTIRs
historical_years = ['LTIR 2020', 'LTIR 2021', 'LTIR 2022', 'LTIR 2023']
predicted_years = ['LTIR 2024', 'LTIR 2025', 'LTIR 2026']

# Make sure you have non-empty values for these columns
historical_values = company_data[historical_years].values.flatten()
predicted_values = company_data[predicted_years].values.flatten()

# Create year labels
years = ['2020', '2021', '2022', '2023', '2024', '2025', '2026']

# Plotting the data
fig, ax = plt.subplots(figsize=(10, 6))

# Historical data plot
ax.plot(historical_years, historical_values, marker="o", label="Historical LTIR", color='blue')

# Predicted data plot (dashed and red)
ax.plot(predicted_years, predicted_values, marker="o", linestyle="dashed", color="red", label="Predicted LTIR")

# Adding labels and title
ax.set_xlabel("Year")
ax.set_ylabel("LTIR")
ax.set_title(f"LTIR Predictions for {selected_company}")
ax.legend()

# Show plot in Streamlit app
st.pyplot(fig)

