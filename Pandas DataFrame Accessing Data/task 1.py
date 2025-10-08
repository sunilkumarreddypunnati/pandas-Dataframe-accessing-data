'''Task 1: Access Columns
Dataset:
data1 = {
    "Product": ["Laptop", "Phone", "Tablet", "Camera"],
    "Price": [60000, 25000, 15000, 30000],
    "Stock": [20, 50, 30, 15]
}

Questions:
Print the Product column.
Print both Product and Price columns.
'''

import pandas as pd
data1 = {
    "Product": ["Laptop", "Phone", "Tablet", "Camera"],
    "Price": [60000, 25000, 15000, 30000],
    "Stock": [20, 50, 30, 15]
}
df=pd.DataFrame(data1)
print("Product column:\n",df['Product'],'\n')
print("Product and Price columns:\n",df[["Product","Price"]])

