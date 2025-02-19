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
  \[ TRIR = {Total Recordable Cases * times 200,000}{\text{Total Hours Worked}}
- Used to assess overall workplace safety.

### **Lost Time Incident Rate (LTIR)**
- A measure of incidents where an employee was unable to work due to injury.
- **Formula:**
  \[ LTIR = \frac{\text{Lost Time Cases} \times 200,000}{\text{Total Hours Worked}} \]
- Focuses on the severity of workplace incidents.
- A Lost Time Case is generally defined as an incident where an employee is unable to work for a full shift or more due to an injury or illness sustained at work.

### **Fatal Accident Rate (FAR)**
- A metric used to measure the number of fatalities per 100 million hours worked.
- Commonly used in high-risk industries such as oil & gas, construction, and manufacturing.
- **Formula:**
  \[ FAR = \frac{\text{Number of Fatalities} \times 100,000,000}{\text{Total Hours Worked}} \]

## Results So Far

### **Model Used**
**RandomForestRegressor**
```python
RandomForestRegressor(n_estimators=100, random_state=42)
```

### **Model Performance (Mean Absolute Error)**
| Cases | Mean Absolute Error |
|-------|---------------------|
| Predicting all 3 KPIs (LTIR, TRIR, FAR) | 0.59 |
| Without FAR | 0.35 |
| Without FAR and LTIR | 0.56 |
| Without FAR and TRIR | 0.107 |

## Next Steps
- Model evaluation (R2, accuracy etc)
- Manage to make the prediction works
- Cross-validation to improve accuracy

## Contributors
- [TheLazyCactus](https://github.com/TheLazyCactus)

## License
This project is open-source and licensed under the MIT License.

