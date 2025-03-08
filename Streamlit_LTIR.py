import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pickle  # Assuming the model is stored as a pickle file
from sklearn.preprocessing import OneHotEncoder

st.write("## BunnyGuard Insurance")
st.write("### Welcome on our portail. This tool help you visualize your LTIR trend for the next 3 years")

# URL of the data
url = 'https://raw.githubusercontent.com/TheLazyCactus/ML_Project/refs/heads/main/final_LTIR_predictions.csv'
df_final = pd.read_csv(url, sep=",", low_memory=False)

#Sort the DataFrame by company names in alphabetical order
df_final_sorted = df_final.sort_values(by='Company', ascending=True)

# Define a short list of companies
companies = df_final_sorted["Company"].unique()

# Dropdown to select a company
selected_company = st.selectbox("Select a Company:", companies)

# Load data for the selected company
company_data = df_final_sorted[df_final_sorted['Company'] == selected_company]

# Display predictions in a table format
st.dataframe(company_data[['LTIR 2021', 'LTIR 2022', 'LTIR 2023', 'LTIR 2024', 'LTIR 2025', 'LTIR 2026']])

# Prepare data for plotting
historical_years = ['2021', '2022', '2023']
predicted_years = ['2024', '2025', '2026']

# Extract historical and predicted values from the DataFrame
historical_values = company_data[['LTIR 2021', 'LTIR 2022', 'LTIR 2023']].values.flatten()
predicted_values = company_data[['LTIR 2024', 'LTIR 2025', 'LTIR 2026']].values.flatten()

# Create year labels for the x-axis
years = historical_years + predicted_years

# Plotting the data
fig, ax = plt.subplots(figsize=(10, 6))

# Historical data plot
ax.plot(historical_years, historical_values[:len(historical_years)], marker="o", label="Historical LTIR", color='blue')

# Predicted data plot (dashed and red)
ax.plot(predicted_years, predicted_values[:len(predicted_years)], marker="o", linestyle="dashed", color="red", label="Predicted LTIR")

# Add labels with values (annotation) at each data point
for i, year in enumerate(historical_years + predicted_years):
    value = historical_values[i] if i < len(historical_years) else predicted_values[i - len(historical_years)]
    ax.annotate(f'{value:.2f}', (year, value), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=8)

# Adding labels and title
ax.set_xlabel("Year")
ax.set_ylabel("LTIR")
ax.set_title(f"LTIR Predictions for {selected_company}")
ax.legend()

# Show the plot in the Streamlit app
st.pyplot(fig)

#Define a short introduction
st.write("Here are some valuable tips to improve your company's LTIR and reduce the risk of work-related incidents:")

# Use st.expander to create expandable sections
with st.expander("1. Implement Comprehensive Safety Training"):
    st.write("""
    Ensure that all employees receive thorough safety training. Offer regular workshops and refresher courses. Educate them about the risks specific to their jobs and how to handle them safely.
    
    **Benefit**: A well-trained workforce is less likely to engage in risky behaviors, leading to fewer injuries.
    """)

with st.expander("2. Promote a Safety-First Culture"):
    st.write("""
    Foster an environment where safety is the top priority. Encourage employees to report hazards and unsafe conditions without fear of repercussions. Establish safety committees to help identify and mitigate risks.
    
    **Benefit**: When employees feel responsible for their own safety and that of their colleagues, the workplace becomes inherently safer.
    """)

with st.expander("3. Conduct Regular Risk Assessments"):
    st.write("""
    Carry out frequent safety audits and risk assessments to identify potential hazards in the workplace. Implement a process for ongoing inspections and immediate resolution of any unsafe conditions.
    
    **Benefit**: Identifying risks before they cause injuries allows the company to address issues proactively and reduce accidents.
    """)

with st.expander("4. Encourage Ergonomics and Proper Equipment Usage"):
    st.write("""
    Invest in ergonomic equipment and ensure that employees are properly trained on how to use it. This is particularly important in workplaces involving repetitive tasks or manual labor.
    
    **Benefit**: Proper ergonomic setups reduce strain-related injuries and improve employee comfort and productivity.
    """)

with st.expander("5. Introduce a Reward Program for Safety Compliance"):
    st.write("""
    Create a rewards program for employees or teams who demonstrate outstanding safety compliance. Offer incentives like bonuses, public recognition, or even extra vacation days for maintaining a safe work environment.
    
    **Benefit**: Positive reinforcement motivates employees to follow safety protocols and helps create a culture of safety.
    """)

with st.expander("6. Establish Clear Emergency Protocols"):
    st.write("""
    Ensure that every employee knows what to do in case of an emergency. Regularly drill emergency evacuation procedures, and maintain first-aid kits, fire extinguishers, and other necessary safety equipment.
    
    **Benefit**: Clear emergency protocols can prevent injuries from escalating in the event of an accident.
    """)

with st.expander("7. Encourage Physical Wellness and Fitness"):
    st.write("""
    Offer wellness programs that focus on physical fitness, stretching, and overall well-being. Employees in better physical condition are less prone to injuries, especially musculoskeletal injuries.
    
    **Benefit**: Healthy employees are less likely to be injured on the job and more likely to recover quickly if an injury occurs.
    """)

with st.expander("8. Implement Job Rotation to Prevent Fatigue"):
    st.write("""
    In jobs that involve repetitive tasks, encourage job rotation to minimize fatigue and overuse injuries. Allow employees to switch tasks regularly to reduce physical strain.
    
    **Benefit**: Reduces long-term strain on muscles and joints, decreasing the likelihood of repetitive stress injuries.
    """)


with st.expander("9. Foster Employee Engagement in Safety Initiatives"):
    st.write("""
    Encourage employees to take ownership of safety by creating a safety suggestion program. Employees who are actively involved in identifying and solving safety problems are more likely to be mindful of their surroundings.
    
    **Benefit**: Engaged employees are more invested in maintaining a safe work environment, which leads to a reduction in accidents.
    """)

with st.expander("10. Set Clear and Measurable Safety Goals"):
    st.write("""
    Establish safety targets and ensure that employees understand their role in achieving these goals. Regularly measure progress and take corrective actions when goals are not being met.
    
    **Benefit**: Having clear goals helps employees stay focused on safety, and it shows them that their actions have an impact on the company's overall safety record.
    """)


st.write("For more guidance please contact [our expert](https://www.linkedin.com/in/valentin-perraud-614420a7).")

st.write("You can also visit our website: ")

# Display a local bunny image at the end
#st.image(r"D:\Documents\GitHub\Bunny_guard.png", caption="Trust our buns!")

from PIL import Image

# Open and resize image
image = Image.open("Bunny_guard.png")
new_size = (300, 500)  # Adjust width and height

st.markdown("<h3 style='text-align: center;'>Trust our buns!</h3>", unsafe_allow_html=True)

# Center using columns
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image(image.resize(new_size))