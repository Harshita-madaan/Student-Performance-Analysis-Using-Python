# Student-Performance-Analysis-Using-Python

📊 Student Performance Analysis using Python

🔍 Project Overview
This project analyzes student academic performance to understand how self-study hours, study efficiency, attendance, and class participation relate to overall performance.
The analysis focuses on honest data interpretation, metric validation, and exploratory data analysis (EDA) using Python, Pandas, NumPy, and Matplotlib.

🎯 Objectives
Analyze the relationship between grades and self-study hours
Evaluate whether study efficiency is a reliable indicator of performance
Examine the impact of class participation on academic outcomes
Practice feature engineering, aggregation, and visualization
Learn to interpret results without forcing conclusions

🗂 Dataset Description
The dataset contains synthetic but realistic generated student performance data with the following columns:
Column Name 	Description
student_id : Unique identifier for each student
weekly_self_study_hours	: Average weekly self-study hours
attendance_percentage	: Attendance percentage
class_participation	: Participation score (0–10)
total_score	: Final academic score (0–100)
grade	Letter : grade derived from total score
Kaggle datasetlink:https://www.kaggle.com/datasets/nabeelqureshitiii/student-performance-dataset

🛠️ Tools & Libraries Used
Python
Pandas
NumPy
Matplotlib

🔧 Feature Engineering
The following new features were created to support deeper analysis:
Performance Category
High (score ≥ 80)
Medium (60 ≤ score < 80)
Low (score < 60)
Study Efficiency
Defined as score per study hour
Later adjusted to handle extreme values and analyzed using median to reduce bias
Attendance Category
Excellent, Good, Poor
Participation Level
High, Medium, Low

📈 Exploratory Data Analysis (EDA)
1️⃣ Grades vs Self-Study Hours
Aggregated average self-study hours per grade
Visualization: Bar chart
Insight:
Higher grades are associated with higher average self-study hours, showing a moderate positive trend.
2️⃣ Study Efficiency vs Performance Category
Initially calculated as score per study hour
Metric refined using smoothing and median aggregation
Key Learning:
Study efficiency alone can be misleading. High-performing students invest more total effort, resulting in better outcomes despite lower efficiency scores.
3️⃣ Class Participation vs Performance Category
Median and mean class participation compared across performance groups
Insight:
Class participation remains nearly constant across performance categories, indicating it does not strongly differentiate academic outcomes in this dataset.

🧠 Key Takeaways
Effort (self-study hours) has a clearer relationship with performance than efficiency
Efficiency metrics must be interpreted carefully
Not all features contribute meaningfully to performance prediction
Honest, flat results are valid analytical outcomes

📌 Conclusion
This project demonstrates the importance of:
Proper feature engineering
Choosing appropriate aggregation metrics
Understanding metric bias
Interpreting results without forcing trends
The analysis reflects real-world data behavior, where not all variables significantly impact outcomes.

🚀 Future Improvements
Add correlation analysis
Explore multivariate relationships
Introduce predictive modeling (regression or classification)
Use real-world datasets for validation
