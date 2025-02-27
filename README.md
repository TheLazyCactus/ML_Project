# Machine Learning Safety KPI Prediction

## Project Goal
This project aims to provide predictions on three key safety KPIs using historical data from the [International Association of Oil & Gas Producers (IOGP)](w) from 2014 to 2023. The three KPIs being predicted are:

- **LTIR (Lost Time Incident Rate)**
- **TRIR (Total Recordable Incident Rate)**
- **FAR (Fatal Accident Rate)**

The final product will allow users to input past safety data from their company and receive predictions for the upcoming years.

## Target Audience
- **Insurance Companies**: For risk assessment and policy pricing.
- **Companies**: To set realistic yearly safety objectives.

## Dataset
The dataset used for this project can be found at:
[ML_Project_safety.csv](https://github.com/TheLazyCactus/ML_Project/blob/main/ML_Project_safety.csv)

## Key Definitions

### **Total Recordable Incident Rate (TRIR)**
- A measure of the number of [OSHA](w)-recordable injuries per 200,000 work hours.
- **Formula:**
   TRIR = {Total Recordable Cases *  200,000} / {Total Hours Worked}
- Used to assess overall workplace safety.

### **Lost Time Incident Rate (LTIR)**
- A measure of incidents where an employee was unable to work due to injury.
- **Formula:**
  LTIR ={Lost Time Cases *  200,000} / {Total Hours Worked}
- Focuses on the severity of workplace incidents.
- A Lost Time Case is generally defined as an incident where an employee is unable to work for a full shift or more due to an injury or illness sustained at work.

### **Fatal Accident Rate (FAR)**
- A metric used to measure the number of fatalities per 100 million hours worked.
- Commonly used in high-risk industries such as oil & gas, construction, and manufacturing.
- **Formula:**
  FAR = {Number of Fatalities *  100,000,000} / {Total Hours Worked}

## Workflow:
1.	Fit ARIMA Models:
   Fit separate ARIMA models for each of the target columns (TRIR total, TRIR company only, and TRIR contractor only).
   For each model, you'll generate predictions and residuals.
2.	Stack ARIMA Predictions and Residuals:
   Add the predictions and residuals for each ARIMA model to the dataset.
3.	Random Forest Model Stacking:
   Use the TRIR total, TRIR company only, and TRIR contractor only ARIMA predictions and residuals as additional features to train a Random Forest model.
   The target variables will be the LTIR total, LTIR company only, and LTIR contractor only.
4.	Prediction:
   The trained Random Forest model will predict LTIR total, LTIR company only, and LTIR contractor only based on the ARIMA features.



## Contributors
- [TheLazyCactus](https://github.com/TheLazyCactus)

## License
This project is open-source and licensed under the MIT License.

