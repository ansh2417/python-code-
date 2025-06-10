import seaborn as sb
import matplotlib.pyplot as plt
import pandas as pd

a = pd.DataFrame({
    'math':[87,58,88,68,25],
    'science':[85,28,15,79,89],
    'english':[88,96,47,65,25]
})


corr = a.corr()

sb.heatmap(corr,annot=True,cmap='viridis')
plt.show()