'''task 3: Specific Cells

Dataset:

data3 = {
    "Student": ["Amit", "Sita", "Raj", "Anu"],
    "Math": [88, 76, 90, 85],
    "Science": [92, 81, 87, 89]
}


Questions:
Math of first student.
Science of student index 2.
Sample Output:

Math score of first student: 88
Science score of student with index 2: 87'''

import pandas as pd
data3 = {
    "Student": ["Amit", "Sita", "Raj", "Anu"],
    "Math": [88, 76, 90, 85],
    "Science": [92, 81, 87, 89]
}
df=pd.DataFrame(data3)
print("Math score of first student:",df.loc[0,"Math"])
print("Science score of student with index 2:"
      ,df.loc[2,"Science"])
