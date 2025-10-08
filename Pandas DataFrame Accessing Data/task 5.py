'''Task 5: Conditional Rows

Dataset:
data5 = {
    "Name": ["Sunil", "Ravi", "Anita", "Priya", "Arjun"],
    "Age": [25, 30, 22, 28, 35],
    "Score": [85, 90, 78, 92, 88]
}
'''

import pandas as pd
data5 = {
    "Name": ["Sunil", "Ravi", "Anita", "Priya", "Arjun"],
    "Age": [25, 30, 22, 28, 35],
    "Score": [85, 90, 78, 92, 88]
}
df=pd.DataFrame(data5)
print("Rows with Age > 25:\n",df[df['Age']>25],'\n')
print("Rows with Score >= 90:\n",df[df["Score"]>=90],'\n')
print("Names of students with Age < 30:\n",
      df.loc[df["Age"]<30,'Name'])
