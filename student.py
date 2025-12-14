import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("/Users/harshita/Desktop/student_performance.csv")
def performance_category(score):
    if score >= 80:
        return "High"
    elif score >= 60:
        return "Medium"
    else:
        return "Low"

df["performance_category"] = df["total_score"].apply(performance_category)

print(df[["total_score", "performance_category"]].head())
print(df["performance_category"].value_counts())
df["study_efficiency"]=df["total_score"]/df["weekly_self_study_hours"]
df["study_efficiency"] = df["study_efficiency"].replace([np.inf, -np.inf], np.nan)
print(df[["total_score","weekly_self_study_hours","study_efficiency"]].head())
print(df["study_efficiency"].describe())
print(df["study_efficiency"].head())

def attendance_category(att):
    if att>=90:
        return "Excellent"
    elif att>=75:
        return "Good"
    else:
        return "Poor"
df["attendance_category"]= df["attendance_percentage"].apply(attendance_category)
print(df[["attendance_percentage","attendance_category"]].head())

def participation_level(score):
    if score>=7:
        return "High"
    elif score>=4:
        return "Med"
    else:
        return "Low"
df["participation_level"]=df["class_participation"].apply(participation_level)
print(df[["class_participation","participation_level"]].head())
print(df.columns)
avg_hrs=df.groupby("grade")["weekly_self_study_hours"].mean()
plt.figure()
plt.bar(avg_hrs.index,avg_hrs.values)
plt.xlabel("Grade")
plt.ylabel("Avg Wekly Self Study Hours")
plt.title("Grades vs Self-Study Hours")
plt.grid(axis='y',linestyle="--")
plt.show(block=False)

avg_efficiency=df.groupby("performance_category")["study_efficiency"].median()

avg_efficiency = avg_efficiency.reindex(["Low", "Medium", "High"])
plt.figure()
plt.bar(avg_efficiency.index,avg_efficiency.values)
plt.xlabel("Performance Category")
plt.ylabel("Average Study Efficiency")
plt.title("Study Efficiency vs Performance Category")
plt.grid(axis='y',linestyle="--")
plt.show(block=False)

avg_class_parti=df.groupby("performance_category")["class_participation"].mean()
plt.figure()
plt.bar(avg_class_parti.index,avg_class_parti.values)
plt.xlabel("Performance Category")
plt.ylabel("Class Participation")
plt.grid(axis='y',linestyle="--")
plt.show()



