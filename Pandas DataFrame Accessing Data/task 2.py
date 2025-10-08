'''Task 2: Access Rows
Dataset:
data2 = {
    "Employee": ["John", "Ravi", "Meena", "Arjun", "Kavya"],
    "Department": ["HR", "IT", "Finance", "IT", "Admin"],
    "Salary": [40000, 60000, 50000, 55000, 45000]
}

Questions:
First row (iloc).
Row index 3 (loc).
'''

import pandas as pd
data2 = {
    "Employee": ["John", "Ravi", "Meena", "Arjun", "Kavya"],
    "Department": ["HR", "IT", "Finance", "IT", "Admin"],
    "Salary": [40000, 60000, 50000, 55000, 45000]
}
df=pd.DataFrame(data2)
print("First row (iloc):\n",df.iloc[0])
print("Row with index 3 (loc):\n",df.loc[3])