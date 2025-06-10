import seaborn as sb
import matplotlib.pyplot as plt
import pandas as pd

a = pd.DataFrame({
    "students":["A","B","C","D"],
    "marks":[56,87,65,79]
})

sb.boxplot(x=a['marks'])
plt.show()