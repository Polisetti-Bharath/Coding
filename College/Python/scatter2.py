import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data={"Age":[23,45,56,23,45,67,89,34,23,45],
      "Income":[50000,60000,80000,45000,70000,120000,90000,75000,52000,68000],
      "Savings":[2000,5000,7000,1500,4000,10000,8000,6000,2500,4500]}
df=pd.DataFrame(data)
sns.scatterplot(data=df,x="Age",y="Income",size="Savings",palette="coolwarm",sizes=(20,200))
plt.title("Age vs Income Scatter Plot")
plt.show()