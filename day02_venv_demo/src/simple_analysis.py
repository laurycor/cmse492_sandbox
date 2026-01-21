import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "category": ["A", "B", "C", "D", "E"],
    "value": [10, 15, 7, 12, 9]
})

print("Mean value:", df["value"].mean())

plt.bar(df["category"], df["value"])
plt.title("Simple Bar Chart Example")
plt.xlabel("Category")
plt.ylabel("Value")
plt.show()
