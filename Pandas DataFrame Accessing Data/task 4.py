'''Task 4: Slice Rows
Dataset:
data4 = {
    "Movie": ["RRR", "KGF", "Pushpa", "Jawan", "Kalki"],
    "Year": [2022, 2022, 2021, 2023, 2024],
    "Collection": [1200, 1100, 800, 1050, 900]
}
Questions:
First 3 rows.
Last 2 rows.

Sample Output:
First 3 rows:
   Movie  Year  Collection
0    RRR  2022        1200
1    KGF  2022        1100
2  Pushpa  2021         800

Last 2 rows:
   Movie  Year  Collection
3  Jawan  2023        1050
4  Kalki  2024         900'''

import pandas as pd
data4 = {
    "Movie": ["RRR", "KGF", "Pushpa", "Jawan", "Kalki"],
    "Year": [2022, 2022, 2021, 2023, 2024],
    "Collection": [1200, 1100, 800, 1050, 900]
}
df=pd.DataFrame(data4)
print("First 3 rows:\n",df.head(3),"\n")
print("Last 2 rows:\n",df.tail(2))