import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Student': ['Ajay', 'Nikita', 'Raj', 'Priya', 'Amit', 'Shreya'],
    'Total_Classes': [50, 50, 50, 50, 50, 50,],
    'Attended_Classes': [45, 48, 39, 42, 20, 30,],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female',]
}

df = pd.DataFrame(data)

df['Attendance (%)'] = (df['Attended_Classes'] / df['Total_Classes']) * 100

df['Satisfactory'] = np.where(df['Attendance (%)'] >= 75, 'Yes', 'No')

print(df)

plt.figure(figsize=(10, 6))
sns.barplot(x='Student', y='Attendance (%)', hue='Satisfactory', data=df, palette='coolwarm')
plt.axhline(75, color='green', linestyle='--', label='75% Threshold')
plt.title("Student Attendance Percentage")
plt.ylabel("Attendance (%)")
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(6, 4))
sns.boxplot(x='Gender', y='Attendance (%)', data=df)
plt.title("Attendance Distribution by Gender")
plt.show()
