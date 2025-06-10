import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = sns.load_dataset('tips')
data['color'] = data['sex'].map({'Male': 'blue', 'Female': 'red'})

plt.figure(figsize=(8, 6))
plt.scatter(
    data['total_bill'],
    data['tip'],
    c=data['color'],
    s=data['size'] * 20,
    alpha=0.7,
    edgecolor='black'
)

plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.title('Total Bill vs Tip (Color: Gender, Size: Party Size)')

for gender, color in {'Male': 'blue', 'Female': 'red'}.items():
    plt.scatter([], [], c=color, label=gender, s=60)
plt.legend(title='Gender')

#plt.grid(True)
plt.tight_layout()
plt.show()