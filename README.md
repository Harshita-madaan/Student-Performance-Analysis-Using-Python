# Student Performance Analysis Using Python

## Project Overview
This project analyzes student academic performance to understand how factors such as self-study hours, attendance, and class participation relate to overall outcomes. The focus is on exploratory data analysis (EDA), feature engineering, and unbiased interpretation of results using Python.

## Objectives

- Analyze the relationship between grades and self-study hours  
- Evaluate the reliability of study efficiency as a performance metric  
- Examine the impact of class participation on academic outcomes  
- Practice feature engineering, aggregation, and data visualization  
- Interpret results without forcing trends or assumptions  

## Dataset

- **Source:** Kaggle  
- **Size:** 1,000,000 rows  
- **Type:** Synthetic but realistic student performance data  
- **Note:** The dataset is pre-cleaned and does not represent real student records  

Dataset Link:  
https://www.kaggle.com/datasets/nabeelqureshitiii/student-performance-dataset

## Tools & Libraries

- Python  
- Pandas  
- NumPy  
- Matplotlib  

## Feature Engineering

The following features were created for deeper analysis:

- Performance Category (High / Medium / Low)  
- Study Efficiency (score per study hour, refined using median aggregation)  
- Attendance Category (Excellent / Good / Poor)  
- Participation Level (High / Medium / Low)  

## Exploratory Data Analysis (EDA)

Key analyses performed:

- **Grades vs Self-Study Hours:** Higher grades show a moderate positive relationship with increased study hours  
- **Study Efficiency vs Performance:** Efficiency alone can be misleading; higher performers invest more total effort  
- **Class Participation vs Performance:** Participation levels remain relatively constant across performance categories  

## Key Takeaways

- Effort (self-study hours) shows a clearer relationship with performance than efficiency  
- Efficiency metrics require careful interpretation  
- Not all features significantly impact performance outcomes  
- Flat or neutral results are valid in real-world data analysis  

## Future Improvements

- Add correlation and multivariate analysis  
- Introduce predictive modeling (regression or classification)  
- Validate findings using real-world datasets  

 
