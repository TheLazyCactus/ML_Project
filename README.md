# Machine Learning Safety KPI Prediction
# BunnyGuard Insurance
This Insurance Portal is an interactive Streamlit web application designed to help companies track, predict, and improve their Lost Time Incident Rate (LTIR). The goal is to provide insightful analytics and motivate businesses to enhance workplace safety, ultimately reducing insurance risks and claims.

## Project Goal
This project aims to provide predictions on three key safety KPIs using historical data from the [International Association of Oil & Gas Producers (IOGP)](w) from 2014 to 2023:
- **LTIR (Lost Time Incident Rate)**

The final product will allow users to input past safety data from their company and receive predictions for the upcoming years.

## Target Audience
- **Insurance Companies**: For risk assessment and policy pricing.
- **Companies**: To set realistic yearly safety objectives.

## Dataset
The dataset used for this project can be found at:
[ML_Project_safety.csv](https://github.com/TheLazyCactus/ML_Project/blob/main/ML_Project_safety.csv)

## Key Definitions

### **Lost Time Incident Rate (LTIR)**
- A measure of incidents where an employee was unable to work due to injury.
- **Formula:**
  LTIR ={Lost Time Cases *  200,000} / {Total Hours Worked}
- Focuses on the severity of workplace incidents.
- A Lost Time Case is generally defined as an incident where an employee is unable to work for a full shift or more due to an injury or illness sustained at work.

## Workflow:

### Features

- LTIR Predictions: Uses a Linear Regression Model to predict LTIR for the next 3 years based on historical data.
- Company Selection: Users can select their company from a dropdown menu to view specific insights.
- Interactive Data Visualization: Line graphs displaying past and future LTIR trends.
- Motivational Safety Tips: Expandable sections providing advice on reducing workplace incidents.
- Bunny Mascot: A fun, friendly bunny displayed at the bottom of the page for encouragement.
- External Resources: Helpful safety guidelines with clickable URLs.

## Data & Model

- Dataset: Historical LTIR values per company.
- Machine Learning Model: Linear Regression trained on past LTIR data to predict future values.
- Feature Engineering: Uses past LTIR values as lag features for forecasting.


## How to Run the App

- pip install streamlit pandas numpy scikit-learn matplotlib
- Run the Streamlit App:
- streamlit run Streamlit_LTIR.py

## How to Use

- Select a company from the dropdown menu.
- View historical LTIR data and predictions for the next three years.
- Explore safety tips by clicking on expandable buttons.
- Check the friendly bunny at the end for a fun touch!

## Future Improvements

- Add more advanced ML models (e.g., Time Series models like ARIMA or LSTM).
- Incorporate real-time data updates.
- Incorporate other KPIs (FAR or TRIR)
- Get more information on the company like type of activities




## Contributors
- [TheLazyCactus](https://github.com/TheLazyCactus)

## License
This project is open-source and licensed under the MIT License.

