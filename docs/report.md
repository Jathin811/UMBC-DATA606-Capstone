# Exploring And Predicting Motor Vehicle Collision In New York City

- Author - Jathin Sathyanath Reddy Toodi
- Semester - Spring'24
- Prepared for UMBC Data Science Master Degree Capstone by Dr Chaojie (Jay) Wang
- GitHub - https://github.com/Jathin811
- LinkedIn - www.linkedin.com/in/toodi-jathin-sathyanath-reddy
- PowerPoint Presentation: https://1drv.ms/p/c/ef985cd12f3f0a03/EQe7hNSAtltOqIeTa9-AycoBpmGT_Ve4Vir9EcnJ6jLbKg?e=Mtc23C 
- YouTube Video: http://www.youtube.com/watch?v=5jvOtGPPUyE


## Background

**What is it about?**  
The chosen topic is vehicular collisions, specifically analyzing a dataset that includes information about the date, time, location, contributing factors, and outcomes (injuries, fatalities) of these collisions. Vehicular collisions are events where two or more vehicles are involved in an accident, often resulting in varying degrees of damage, injuries, or even fatalities. Understanding the patterns, factors, and outcomes of these collisions is crucial for promoting road safety, improving traffic management, and implementing preventive measures.

**Why does it matter?**  
This project matters because it provides valuable insights into the dynamics of vehicular collisions. By analyzing the data, we can identify trends, contributing factors, and high-risk areas, ultimately contributing to the development of strategies to reduce accidents and enhance overall road safety.

**What are your research questions?**  
1. What are the temporal trends in vehicular collisions over the specified time period?
2. Which boroughs or zip codes exhibit the highest frequency of collisions?
3. Are there specific times of the day when collisions are more likely to occur?
4. What is the distribution of injuries and fatalities among persons, pedestrians, cyclists, and motor vehicle occupants?
5. What are the most common contributing factors to vehicular collisions?
6. Which types of vehicles are most frequently involved in collisions?

## Data

**Describing my dataset.**

**Data sources:** [Motor Vehicle Collisions - Crashes](https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Crashes/h9gi-nx95/about_data)

**Data size:** 418MB

**Data shape:** 2.06 million rows and 29 columns

**Time period:** April 28, 2014, to present

**What does each row represent:** Accident data

**Data dictionary:**

1. **CRASH DATE:**
   - Description: Occurrence date of collision
   - Type: Date & Time

2. **CRASH TIME:**
   - Description: Occurrence time of collision
   - Type: Plain Text

3. **BOROUGH:**
   - Description: Borough where collision occurred
   - Type: Plain Text

4. **ZIP CODE:**
   - Description: Postal code of incident occurrence
   - Type: Plain Text

5. **LATITUDE:**
   - Description: Latitude coordinate for Global Coordinate System, WGS 1984, decimal degrees (EPSG 4326)
   - Type: Number

6. **LONGITUDE:**
   - Description: Longitude coordinate for Global Coordinate System, WGS 1984, decimal degrees (EPSG 4326)
   - Type: Number

7. **LOCATION:**
   - Description: Latitude , Longitude pair
   - Type: Location

8. **ON STREET NAME:**
   - Description: Street on which the collision occurred
   - Type: Plain Text

9. **CROSS STREET NAME:**
   - Description: Nearest cross street to the collision
   - Type: Plain Text

10. **OFF STREET NAME:**
    - Description: Street address if known
    - Type: Plain Text

11. **NUMBER OF PERSONS INJURED:**
    - Description: Number of persons injured
    - Type: Number

12. **NUMBER OF PERSONS KILLED:**
    - Description: Number of persons killed
    - Type: Number

13. **NUMBER OF PEDESTRIANS INJURED:**
    - Description: Number of pedestrians injured
    - Type: Number

14. **NUMBER OF PEDESTRIANS KILLED:**
    - Description: Number of pedestrians killed
    - Type: Number

15. **NUMBER OF CYCLIST INJURED:**
    - Description: Number of cyclists injured
    - Type: Number

16. **NUMBER OF CYCLIST KILLED:**
    - Description: Number of cyclists killed
    - Type: Number

17. **NUMBER OF MOTORIST INJURED:**
    - Description: Number of vehicle occupants injured
    - Type: Number

18. **NUMBER OF MOTORIST KILLED:**
    - Description: Number of vehicle occupants killed
    - Type: Number

19. **CONTRIBUTING FACTOR VEHICLE 1:**
    - Description: Factors contributing to the collision for designated vehicle
    - Type: Plain Text

20. **CONTRIBUTING FACTOR VEHICLE 2:**
    - Description: Factors contributing to the collision for designated vehicle
    - Type: Plain Text

21. **CONTRIBUTING FACTOR VEHICLE 3:**
    - Description: Factors contributing to the collision for designated vehicle
    - Type: Plain Text

22. **CONTRIBUTING FACTOR VEHICLE 4:**
    - Description: Factors contributing to the collision for designated vehicle
    - Type: Plain Text

23. **CONTRIBUTING FACTOR VEHICLE 5:**
    - Description: Factors contributing to the collision for designated vehicle
    - Type: Plain Text

24. **COLLISION_ID:**
    - Description: Unique record code generated by the system. Primary Key for Crash table.
    - Type: Number

25. **VEHICLE TYPE CODE 1:**
    - Description: Type of vehicle based on the selected vehicle category (ATV, bicycle, car/suv, ebike, escooter, truck/bus, motorcycle, other)
    - Type: Plain Text

26. **VEHICLE TYPE CODE 2:**
    - Description: Type of vehicle based on the selected vehicle category (ATV, bicycle, car/suv, ebike, escooter, truck/bus, motorcycle, other)
    - Type: Plain Text

27. **VEHICLE TYPE CODE 3:**
    - Description: Type of vehicle based on the selected vehicle category (ATV, bicycle, car/suv, ebike, escooter, truck/bus, motorcycle, other)
    - Type: Plain Text

28. **VEHICLE TYPE CODE 4:**
    - Description: Type of vehicle based on the selected vehicle category (ATV, bicycle, car/suv, ebike, escooter, truck/bus, motorcycle, other)
    - Type: Plain Text

29. **VEHICLE TYPE CODE 5:**
    - Description: Type of vehicle based on the selected vehicle category (ATV, bicycle, car/suv, ebike, escooter, truck/bus, motorcycle, other)
    - Type: Plain Text
- **Target Variable(s)** - Number of deaths is Target Variable
- NUMBER OF PERSONS INJURED,
NUMBER OF PEDESTRIANS KILLED,NUMBER OF CYCLIST KILLED,NUMBER OF MOTORIST INJURED,NUMBER OF MOTORIST KILLED,CONTRIBUTING FACTOR VEHICLE 1,COLLISION_ID,NUMBER OF PERSONS KILLED are predictors

## Model Training
1. Models for Predictive Analytics:
Models used are Linear regression, Decision trees, Random forest.
2. Training Procedure:
I have performed the Train vs test split for 80/20 to ensure the model learns effectively and generalizes well to new data.

3. Python Packages:
I have primarily used python packages in project. They are Numpy, Pandas,matplotlib, plotly, seaborn and scikit-learn

4. Development Environments:
The development environments are
- Local machine: Jupyter Notebook 
- Online platforms: Google Colab, GitHub

5.Performance Measures of the models
The performance of the models was evaluated using various metrics, including:

Accuracy: Measures the proportion of correctly classified instances.
By assessing these performance measures, the effectiveness of each model in predicting outcomes was evaluated, providing insights into their strengths and weaknesses.
By seeing the results of models they performed very good in predicting the number of deaths.

**Linear Regression:**
- Achieved an accuracy of 98.05% on the training set and 97.89% on the test set.
- Demonstrated high precision with minimal errors, as indicated by zero mean absolute, mean squared, and root mean squared errors.
- Exhibited a high R-squared value of 0.98, indicating strong predictive capability.
- Summary: The linear regression model showed outstanding accuracy and precision in predicting the target variable.

**Decision Tree Regressor:**
- Attained perfect accuracy of 100.0% on the training set and 95.51% on the test set.
-  Showed negligible errors with zero mean absolute, mean squared, and root mean squared errors.
- Achieved a commendable R-squared value of 0.96, indicating robust predictive performance.
- Summary: The decision tree regressor model demonstrated flawless accuracy on the training set and high accuracy on the test set, making it highly reliable for prediction tasks.
  
**Random Forest Regressor:**
- Achieved an accuracy of 99.63% on the training set and 95.70% on the test set.
- Displayed minimal errors with zero mean absolute, mean squared, and root mean squared errors.
- Maintained a strong R-squared value of 0.96, highlighting its predictive prowess.
- Summary: The random forest regressor model exhibited robust predictive performance with high accuracy on both training and test sets, making it highly effective for prediction tasks.


## Web App Development:
Developed a web application using Streamlit for users to interact with accident trends.
## Features:

1. **Map Display:**
   - Users can visualize locations where a specified number of people were injured in collisions on a map.
   
2. **Time Analysis:**
   - Users can select an hour, and the app displays a hexagonal heatmap representing the density of collisions during that hour.
   - Additionally, it provides a breakdown by minute within the selected hour to understand temporal trends.

3. **Top Risky Streets:**
   - Displays the top 5 streets with the highest number of injuries to pedestrians, cyclists, or motorists, based on user selection.

4. **Raw Data Display:**
   - Optionally, users can view the raw data used for analysis.
## Conclusion:

- The project's primary objective was to enhance road safety and prevent accidents by leveraging data-driven insights.
- A comprehensive dataset of vehicle collisions and accidents was analyzed to understand patterns and contributing factors.
- Thorough analysis and modeling techniques were employed to extract valuable insights from the dataset.
- These insights enabled the development of recommendations aimed at improving road safety measures.
- This provides  actionable recommendations to prevent future collisions based on the analysis findings.

